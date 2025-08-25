from .base import *

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/secret_key/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS = ['staging.comtura.de']

# Development-specific settings
INTERNAL_IPS = ['127.0.0.1']

# Disable security settings for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
