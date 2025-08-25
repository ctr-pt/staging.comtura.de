from .base import *
import os

DEBUG = True  # Für Staging noch Debug aktiviert
SECRET_KEY = 'django-insecure-staging-key-for-staging-only'

ALLOWED_HOSTS = ['staging.comtura.de']
WAGTAILADMIN_BASE_URL = 'https://staging.comtura.de/cms_admin'

# Staging-specific settings
INTERNAL_IPS = ['127.0.0.1']

# PostgreSQL Database für Staging
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'staging.comtura.de',
        'USER': 'ctr_database',
        'PASSWORD': '2025ctr_saZbyTARMTZ4DhmW',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': 60,
        },
    }
}

# Moderate Security für Staging
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Staging-spezifische Email-Settings (falls gewünscht)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Emails in Console

ROOT_URLCONF = 'comtura_main.urls'
