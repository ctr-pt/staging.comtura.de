from .base import *
import os

DEBUG = False

# Production secret key from file
try:
    with open('/etc/secret_key/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
except FileNotFoundError:
    raise Exception('Secret key file not found!')

ALLOWED_HOSTS = ['comtura.de']
CSRF_TRUSTED_ORIGINS = ['https://comtura.de']

# Production Database (PostgreSQL recommended)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'staging_comtura'),
        'USER': os.getenv('DB_USER', 'comtura_user'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Security settings
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email settings for production
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', 'production-password')
