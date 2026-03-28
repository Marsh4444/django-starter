"""
config/settings/dev.py

Development-only settings.
Run with: python manage.py runserver --settings=config.settings.dev
Or set DJANGO_SETTINGS_MODULE=config.settings.dev in your .env
"""

from .base import *

# ─────────────────────────────────────────
# DEVELOPMENT OVERRIDES
# ─────────────────────────────────────────
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Use SQLite in dev if you want a quick start (optional)
# Comment this out to use PostgreSQL from base.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Django Debug Toolbar (install separately: pip install django-debug-toolbar)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
# INTERNAL_IPS = ['127.0.0.1']

# Email — print to console in dev instead of sending real emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
