from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

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

# Custom Blocks für die Content-Seite
class CarouselBlock(blocks.StructBlock):
    """Carousel/Slider Block"""
    title = blocks.CharBlock(required=False, help_text="Titel für den Carousel")
    
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link_url', blocks.URLBlock(required=False, help_text="Link-Ziel")),
            ('link_text', blocks.CharBlock(required=False, help_text="Link-Text")),
        ]),
        help_text="Fügen Sie Slides hinzu"
    )
    
    class Meta:
        template = 'blocks/carousel_block.html'
        icon = 'image'
        label = 'Carousel'

class CardBlock(blocks.StructBlock):
    """Card Block für mehrere Cards nebeneinander"""
    title = blocks.CharBlock(required=False, help_text="Titel für die Card-Sektion")
    
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link_url', blocks.URLBlock(required=False)),
            ('link_text', blocks.CharBlock(required=False, default="Mehr erfahren")),
            ('icon_class', blocks.CharBlock(required=False, help_text="Font Awesome Icon (z.B. fas fa-rocket)")),
        ]),
        help_text="Fügen Sie Cards hinzu"
    )
    
    cards_per_row = blocks.ChoiceBlock(
        choices=[
            ('2', '2 Cards pro Reihe'),
            ('3', '3 Cards pro Reihe'),
            ('4', '4 Cards pro Reihe'),
        ],
        default='3'
    )
    
    class Meta:
        template = 'blocks/card_block.html'
        icon = 'grip'
        label = 'Cards'

class MapBlock(blocks.StructBlock):
    """Google Maps Block"""
    title = blocks.CharBlock(required=False, help_text="Titel für die Karte")
    address = blocks.CharBlock(required=True, help_text="Adresse die angezeigt werden soll")
    map_width = blocks.IntegerBlock(default=100, help_text="Breite in Prozent")
    map_height = blocks.IntegerBlock(default=400, help_text="Höhe in Pixel")
    zoom_level = blocks.IntegerBlock(default=15, help_text="Zoom-Level (1-20)")
    
    class Meta:
        template = 'blocks/map_block.html'
        icon = 'site'
        label = 'Karte'

class ContactFormBlock(blocks.StructBlock):
    """Kontaktformular Block"""
    title = blocks.CharBlock(default="Kontaktformular", help_text="Titel für das Formular")
    intro_text = blocks.TextBlock(required=False, help_text="Einführungstext")
    success_message = blocks.CharBlock(default="Vielen Dank für Ihre Nachricht!", help_text="Erfolgsmeldung")
    
    class Meta:
        template = 'blocks/contact_form_block.html'
        icon = 'mail'
        label = 'Kontaktformular'

class VideoBlock(blocks.StructBlock):
    """Video Block"""
    title = blocks.CharBlock(required=False, help_text="Titel für das Video")
    video = EmbedBlock(help_text="YouTube, Vimeo oder andere Video-URL")
    caption = blocks.TextBlock(required=False, help_text="Video-Beschreibung")
    
    class Meta:
        template = 'blocks/video_block.html'
        icon = 'media'
        label = 'Video'

class QuoteBlock(blocks.StructBlock):
    """Zitat/Testimonial Block"""
    quote_text = blocks.TextBlock(required=True, help_text="Der Zitat-Text")
    author = blocks.CharBlock(required=True, help_text="Autor des Zitats")
    author_title = blocks.CharBlock(required=False, help_text="Position/Titel des Autors")
    author_company = blocks.CharBlock(required=False, help_text="Unternehmen des Autors")
    author_image = ImageChooserBlock(required=False, help_text="Foto des Autors")
    
    class Meta:
        template = 'blocks/quote_block.html'
        icon = 'openquote'
        label = 'Zitat'

class StatsBlock(blocks.StructBlock):
    """Statistiken/Zahlen Block"""
    title = blocks.CharBlock(required=False, help_text="Titel für die Statistik-Sektion")
    
    stats = blocks.ListBlock(
        blocks.StructBlock([
            ('number', blocks.CharBlock(required=True, help_text="Zahl (z.B. 500+)")),
            ('label', blocks.CharBlock(required=True, help_text="Beschreibung")),
            ('icon_class', blocks.CharBlock(required=False, help_text="Font Awesome Icon")),
        ]),
        help_text="Fügen Sie Statistiken hinzu"
    )
    
    class Meta:
        template = 'blocks/stats_block.html'
        icon = 'list-ol'
        label = 'Statistiken'

# Content Page Model
class ContentPage(Page):
    """Flexible Content-Seite mit StreamField-Blöcken"""
    
    intro_text = RichTextField(blank=True, help_text="Einführungstext (optional)")
    
    content_blocks = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('carousel', CarouselBlock()),
        ('cards', CardBlock()),
        ('map', MapBlock()),
        ('contact_form', ContactFormBlock()),
        ('video', VideoBlock()),
        ('quote', QuoteBlock()),
        ('stats', StatsBlock()),
        ('html', blocks.RawHTMLBlock(icon='code', label='HTML Code')),
    ], blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
        FieldPanel('content_blocks'),
    ]
    
    class Meta:
        verbose_name = "Content-Seite"
        verbose_name_plural = "Content-Seiten"