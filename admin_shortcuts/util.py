import os

from django.contrib.staticfiles.templatetags.staticfiles import static

try:
    from django.utils.encoding import smart_bytes
except ImportError:
    # Django < 1.5 so no Python 3 support
    smart_bytes = bytes


def generate_javascript_tag(filename):
    url = static(os.path.join('django_admin_shortcuts', 'js', filename))
    return b'<script src="' + smart_bytes(url) + b'" type="text/javascript"></script>'


def generate_css_tag(filename):
    url = static(os.path.join('django_admin_shortcuts', 'css', filename))
    return b'<link rel="stylesheet" href="' + smart_bytes(url) + b'" type="text/css">'
