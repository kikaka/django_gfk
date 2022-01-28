"""
WSGI config for event_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from .utils import getenv

env = getenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', env("SETTINGS_MODULE"))

application = get_wsgi_application()
