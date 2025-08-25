from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks

class HomePage(Page):
    """Startseite - comtura.de"""
    intro_title = models.CharField(
        max_length=100, 
        default="Ihr strategischer IT-Dienstleister",
        help_text="Haupt-Überschrift"
    )
    
    intro_text = RichTextField(
        blank=True,
        help_text="Einführungstext zur Firma"
    )
    
    company_description = RichTextField(
        blank=True,
        help_text="Hauptbeschreibung des Unternehmens"
    )
    
    standorte_text = RichTextField(
        blank=True,
        help_text="Text über die Standorte"
    )
    
    portfolio_items = StreamField([
        ('portfolio_item', blocks.RichTextBlock()),
    ], blank=True, help_text="Portfolio-Punkte mit ■ Symbol", use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_title'),
        FieldPanel('intro_text'),
        FieldPanel('company_description'),
        FieldPanel('standorte_text'),
        FieldPanel('portfolio_items'),
    ]
    
    class Meta:
        verbose_name = "Homepage"

class ServicePage(Page):
    """Service-Seiten (Projektleitung, IT-Bau, etc.)"""
    service_content = RichTextField(
        blank=True,
        help_text="Haupt-Content der Service-Seite"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('service_content'),
    ]
    
    class Meta:
        verbose_name = "Service-Seite"

class JobListingPage(Page):
    """Stellenangebote-Hauptseite"""
    intro_text = RichTextField(
        blank=True,
        default="<h3>Übersicht freier Stellen</h3>"
    )
    
    requirements = StreamField([
        ('requirement', blocks.RichTextBlock()),
    ], blank=True, help_text="Anforderungen mit ■ Symbol", use_json_field=True)
    
    closing_text = RichTextField(
        blank=True,
        default="<p><strong>Dann bewerben Sie sich jetzt....</strong></p>"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
        FieldPanel('requirements'),
        FieldPanel('closing_text'),
    ]
    
    class Meta:
        verbose_name = "Stellenangebote-Übersicht"

class JobPage(Page):
    """Einzelne Stellenausschreibung"""
    job_description = RichTextField(blank=True, help_text="Stellenbeschreibung")
    what_we_offer = RichTextField(blank=True, help_text="Was wir bieten")
    your_profile = RichTextField(blank=True, help_text="Ihr Profil") 
    your_tasks = RichTextField(blank=True, help_text="Ihre Aufgaben")
    
    content_panels = Page.content_panels + [
        FieldPanel('job_description'),
        FieldPanel('what_we_offer'),
        FieldPanel('your_profile'),
        FieldPanel('your_tasks'),
    ]
    
    parent_page_types = ['homepage.JobListingPage']
    
    class Meta:
        verbose_name = "Stellenausschreibung"

class ContactPage(Page):
    """Kontakt-Seite"""
    contact_intro = RichTextField(
        blank=True,
        help_text="Einführungstext für Kontaktseite"
    )
    
    # Firmeninformationen
    company_name = models.CharField(
        max_length=200,
        default="comtura IT-Servicegesellschaft für Industrie und Handel"
    )
    
    owner_name = models.CharField(
        max_length=100,
        default="Ralph Herrmann",
        help_text="Geschäftsführer"
    )
    
    # Hauptsitz
    main_address = models.TextField(
        default="Möslestr. 36\nD-79276 Reute",
        help_text="Hauptsitz-Adresse"
    )
    
    # Verwaltung
    admin_address = models.TextField(
        default="Gartenstr. 20a\n79312 Emmendingen",
        help_text="Verwaltung und Lager"
    )
    
    phone = models.CharField(max_length=50, default="+49 (0)7641-937 24 30")
    fax = models.CharField(max_length=50, default="+49 (0)7641-937 24 32")
    email = models.EmailField(default="verwaltung@comtura.de")
    
    content_panels = Page.content_panels + [
        FieldPanel('contact_intro'),
        FieldPanel('company_name'),
        FieldPanel('owner_name'),
        FieldPanel('main_address'),
        FieldPanel('admin_address'),
        FieldPanel('phone'),
        FieldPanel('fax'),
        FieldPanel('email'),
    ]
    
    class Meta:
        verbose_name = "Kontakt-Seite"

class ImpressumPage(Page):
    """Impressum"""
    impressum_content = RichTextField(
        blank=True,
        help_text="Impressum-Inhalt"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('impressum_content'),
    ]
    
    class Meta:
        verbose_name = "Impressum"
