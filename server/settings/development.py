from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', 'localhost:8000', '127.0.0.1', '127.0.0.1:8000']

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_VERIFICATION = 'none'