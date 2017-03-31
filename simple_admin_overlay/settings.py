from django.conf import settings
from django.utils.lru_cache import lru_cache


CONFIG_DEFAULTS = {
    'OVERLAY_POSITION': 'top',
    'DEFAULT_STATE': 'open',
    'SHOW_APPS_ONLY': False,
    'EXCLUDE_APPS': [],
    'EXCLUDE_MODELS': {},
}


@lru_cache()
def get_config():
    USER_CONFIG = getattr(settings, 'SIMPLE_ADMIN_OVERLAY_CONFIG', {})

    CONFIG = CONFIG_DEFAULTS.copy()
    CONFIG.update(USER_CONFIG)

    return CONFIG
