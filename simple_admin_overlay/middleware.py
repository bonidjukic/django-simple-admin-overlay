"""
Django Simple Admin Overlay middleware
"""

import re
import django.contrib.admin as admin
import simple_admin_overlay.util as util
import simple_admin_overlay.settings as al_settings

from django.core.urlresolvers import NoReverseMatch, reverse
from django.template.loader import render_to_string


try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    MiddlewareMixin = object


_HTML_TYPES = ('text/html', 'application/xhtml+xml')


class SimpleAdminOverlayMiddleware(MiddlewareMixin):
    """
    Middleware to display the admin links on frontend pages.
    """

    allowed_status_codes = (200,)
    allowed_content_types = ('text/html', 'application/xhtml+xml')
    template = 'simple_admin_overlay.html'

    def process_response(self, request, response):
        """
        Insert necessary javascript to set admin overlay
        """

        if self.is_regular_page(request, response) and self.can_show_overlay(request, response):
            self.insert_overlay(request, response)
        return response

    def is_regular_page(self, request, response):
        return response.status_code in self.allowed_status_codes \
           and not request.is_ajax() \
           and response['Content-Type'].split(';')[0] in self.allowed_content_types

    def can_show_overlay(self, request, response):
        """
        Check whether the current visitor should see the overlay
        """
        return self.is_valid_user(request) and self.is_frontend_page(request)

    @staticmethod
    def is_valid_user(request):
        return hasattr(request, 'user') \
           and request.user.is_authenticated() \
           and request.user.is_staff

    @staticmethod
    def is_frontend_page(request):
        try:
            return not request.path.startswith(reverse('admin:index'))
        except NoReverseMatch:
            return True

    def insert_overlay(self, request, response):
        """
        Insert the overlay into the response.
        """

        if not getattr(response, 'streaming', False):
            is_gzipped = 'gzip' in response.get('Content-Encoding', '')
            is_html = response.get('Content-Type', '').split(';')[0] in _HTML_TYPES

            if is_html and not is_gzipped:
                head_pattern = re.compile(b'</head>', re.IGNORECASE)
                body_pattern = re.compile(b'</body>', re.IGNORECASE)

                head_tags = util.generate_javascript_tag('simple_admin_overlay.js') + \
                            util.generate_css_tag('simple_admin_overlay.css')
                response.content = head_pattern.sub(head_tags + b'</head>', response.content)

                template = render_to_string(self.template,
                                            self.get_context_data(request)).encode('utf-8')
                response.content = body_pattern.sub(template + b'</body>', response.content)

                if response.get('Content-Length', None):
                    response['Content-Length'] = len(response.content)

        return response

    def get_context_data(self, request):
        al_settings_config = al_settings.get_config()

        return {
            'app_list': admin.site.get_app_list(request),
            'overlay_position': al_settings_config['OVERLAY_POSITION'],
            'default_state': al_settings_config['DEFAULT_STATE'],
            'show_apps_only': al_settings_config['SHOW_APPS_ONLY'],
        }
