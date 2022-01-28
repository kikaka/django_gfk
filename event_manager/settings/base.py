"""
Django settings for event_manager project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from ..utils import getenv
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = getenv()

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
INTERNAL_IPS = env.list("INTERNAL_IPS")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
]

INSTALLED_APPS.extend(["events", "user"])

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "event_manager" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'event_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True
USE_L10N = True  # Zahlenformate (locale)
USE_TZ = True

AUTH_USER_MODEL = 'user.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",

}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(module)s %(asctime)s %(pathname)s%(message)s"
        },
    },
    "handlers": {
        # an die MAil Admins gehen nur ERRORs
        # außerdem muss debug explizit FALSE sein
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        # live kommen nach debug_log nur Warnings. trotzdem definieren wir hier
        # DEBUG, damit wir auch DEBUG Messages schreiben können beim dev.
        "debug_log": {
            "level": "DEBUG",
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 50000,
            'backupCount': 1,
            "filename": BASE_DIR / "debug.log",
            "formatter": "simple",
        },
        # ins django_log file kommen generell nur mindestens warnings
        "django_log": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "django_errors.log",
            "formatter": "simple",
        },
        # Auf die console können wir auch Infos schreiben
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            'level': 'INFO',
            'filters': ['require_debug_true'],
        },

    },
    "root": {"handlers": ["console"], "level": "WARNING"},
    # um doppeltes Loggen mit dem Root Logger zu vermeiden, setzen wir
    # prograte auf False überall
    "loggers": {
        "django": {
            "handlers": ["django_log", "mail_admins", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "event_manager.events": {
            "handlers": ["debug_log"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}
