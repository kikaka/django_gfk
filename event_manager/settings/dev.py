from debug_toolbar.panels.logging import collector
from event_manager.settings.base import *


INSTALLED_APPS.extend(['debug_toolbar', 'django_extensions'])

MIDDLEWARE.extend(["debug_toolbar.middleware.DebugToolbarMiddleware",
                  "event_manager.middleware.PerfCountMiddleware"])

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

LOGGING["handlers"].update(
    {
        "djdt_log": {
            "level": "DEBUG",
            "class": "debug_toolbar.panels.logging.ThreadTrackingHandler",
            "collector": collector,
        },
    }
)

LOGGING["loggers"].update(
    {
        "event_manager.events": {
            "handlers": ["debug_log", "console", "djdt_log"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django": {
            "handlers": ["django_log", "console", "djdt_log"],
            "level": "WARNING",
            "propagate": True,
        },
    }
)
