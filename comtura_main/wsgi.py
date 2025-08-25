import os
from django.core.wsgi import get_wsgi_application

# Für aktuelles Staging-System
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comtura_main.settings.staging')
application = get_wsgi_application()
