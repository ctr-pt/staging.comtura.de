from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure-dev-key-for-development-only'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Development-specific settings
INTERNAL_IPS = ['127.0.0.1']

# Disable security settings for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
