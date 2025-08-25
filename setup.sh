#!/bin/bash
# Setup-Script für comtura Django/Wagtail-Projekt

echo "🚀 Setup für comtura IT-Servicegesellschaft"
echo "==========================================="

# Virtual Environment erstellen wenn nicht vorhanden
if [ ! -d "venv" ]; then
    echo "📦 Erstelle Virtual Environment..."
    python3 -m venv venv
fi

# Virtual Environment aktivieren
echo "🔧 Aktiviere Virtual Environment..."
source venv/bin/activate

# Dependencies installieren
echo "📚 Installiere Dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Datenbank migrieren
echo "💾 Führe Datenbank-Migrationen durch..."
python manage.py makemigrations
python manage.py migrate

# Plugin-Setup ausführen
echo "🧩 Setup Plugins und Gruppen..."
python manage.py setup_plugins

# Static files sammeln für Development
echo "🎨 Sammle Static Files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ Setup abgeschlossen!"
echo ""
echo "Nächste Schritte:"
echo "1. Superuser erstellen: python manage.py createsuperuser"
echo "2. Development Server starten: python manage.py runserver"
echo "3. Browser öffnen: http://127.0.0.1:8000"
echo ""
echo "📝 Wagtail Admin: http://127.0.0.1:8000/cms-admin/"
echo "📊 Django Admin: http://127.0.0.1:8000/ctr_admin/"
echo "🏠 Homepage: http://127.0.0.1:8000/"
