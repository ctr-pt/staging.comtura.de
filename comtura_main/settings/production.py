from .base import *
import os

DEBUG = False

# Production secret key from file
try:
    with open('/etc/secret_key/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
except FileNotFoundError:
    raise Exception('Secret key file not found!')

ALLOWED_HOSTS = ['comtura.de', 'www.comtura.de']
CSRF_TRUSTED_ORIGINS = ['https://comtura.de', 'https://www.comtura.de']

# Production Database (separate DB für Production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'comtura.de',  # Separate Production DB
        'USER': 'ctr_production',  # Separate Production User
        'PASSWORD': os.getenv('PROD_DB_PASSWORD'),  # Aus Environment
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': 60,
        },
    }
}

# Maximale Security für Production
SECURE_HSTS_SECONDS = 31536000  # 1 Jahr
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Production Email Settings
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', 'production-password')
