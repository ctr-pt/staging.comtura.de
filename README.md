# comtura IT-Servicegesellschaft - Django/Wagtail Projekt

Ein professionelles Django/Wagtail-basiertes System für die comtura IT-Servicegesellschaft mit Plugin-Architektur für verschiedene Geschäftsbereiche.

## Features

- **Corporate Homepage** basierend auf comtura.de
- **Plugin-System** für modulare Funktionen
- **Rollenbasierte Zugriffskontrolle**
- **Bootstrap-Design** mit Corporate Identity
- **Responsive Design** für alle Geräte

## Plugins

- **Leistungsnachweis**: Digitale Leistungsnachweise mit PDF-Generation
- **Zeiterfassung**: Timer-basierte Zeiterfassung
- **Lager-Management**: Bestandsverwaltung und Warenwirtschaft  
- **Ticket-System**: Support-Ticket-Verwaltung

## Installation

1. **Virtual Environment erstellen**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # oder
   venv\Scripts\activate  # Windows
   ```

2. **Dependencies installieren**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Datenbank migrieren**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Superuser erstellen**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Initial Setup**:
   ```bash
   python manage.py setup_plugins
   ```

6. **Development Server starten**:
   ```bash
   python manage.py runserver
   ```

## Deployment

Für Production-Deployment mit Apache/mod_wsgi:

1. **Settings anpassen**: `comtura_main/settings/production.py`
2. **Static Files sammeln**: `python manage.py collectstatic`
3. **Apache Virtual Host konfigurieren**
4. **SSL-Zertifikat mit Let's Encrypt einrichten**

## Struktur

```
staging_comtura/
├── comtura_main/          # Django-Projekt-Einstellungen
├── apps/
│   ├── homepage/          # Wagtail Homepage
│   ├── common/           # Geteilte Models
│   ├── plugins/          # Plugin-System
│   ├── leistungsnachweis/ # Report-System
│   ├── zeiterfassung/     # Timer-System
│   ├── stockmgmt/        # Lager-Management
│   └── ticketsystem/     # Ticket-System
├── templates/            # Django-Templates
├── static/              # CSS, JS, Images
└── media/              # User-Uploads
```

## Benutzergruppen

- **employees**: Vollzugriff auf alle Plugins
- **contractors**: Leistungsnachweis + Zeiterfassung
- **customers**: Nur Ticket-System
- **admins**: Vollzugriff + Admin-Rechte

## Support

Bei Fragen oder Problemen wenden Sie sich an den System-Administrator.
