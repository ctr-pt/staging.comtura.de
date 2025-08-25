from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    intro_text = RichTextField(blank=True, help_text="Einführungstext für die Startseite")
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
    ]
    
    class Meta:
        verbose_name = "Homepage"

class ServicePage(Page):
    service_content = RichTextField(blank=True, help_text="Inhalt der Service-Seite")
    
    content_panels = Page.content_panels + [
        FieldPanel('service_content'),
    ]
    
    class Meta:
        verbose_name = "Service-Seite"
