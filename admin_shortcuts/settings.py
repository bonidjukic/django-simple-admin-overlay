from django.conf import settings
from django.utils.lru_cache import lru_cache


CONFIG_DEFAULTS = {
    'TOOLBAR_POSITION': 'top',
    'DEFAULT_STATE': 'open',
}


@lru_cache()
def get_config():
    USER_CONFIG = getattr(settings, 'ADMIN_SHORTCUTS_CONFIG', {})

    CONFIG = CONFIG_DEFAULTS.copy()
    CONFIG.update(USER_CONFIG)

    return CONFIG
