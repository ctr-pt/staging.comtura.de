from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
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

# --- Block-Definitionen ---

class CarouselBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link_url', blocks.URLBlock(required=False)),
            ('link_text', blocks.CharBlock(required=False)),
        ])
    )
    
    class Meta:
        template = 'blocks/carousel_block.html'
        icon = 'image'
        label = 'Carousel'

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link_url', blocks.URLBlock(required=False)),
            ('link_text', blocks.CharBlock(required=False, default="Mehr erfahren")),
            ('icon_class', blocks.CharBlock(required=False)),
        ])
    )
    
    cards_per_row = blocks.ChoiceBlock(
        choices=[('2', '2 Spalten'), ('3', '3 Spalten'), ('4', '4 Spalten')],
        default='3'
    )

    class Meta:
        template = 'blocks/card_block.html'
        icon = 'grip'
        label = 'Cards'

class MapBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    address = blocks.CharBlock(required=True)
    map_width = blocks.IntegerBlock(default=100)
    map_height = blocks.IntegerBlock(default=400)
    zoom_level = blocks.IntegerBlock(default=15)
    class Meta:
        template = 'blocks/map_block.html'
        icon = 'site'
        label = 'Map'

class ContactFormBlock(blocks.StructBlock):
    title = blocks.CharBlock(default="Kontaktformular")
    intro_text = blocks.TextBlock(required=False)
    success_message = blocks.CharBlock(default="Vielen Dank für Ihre Nachricht!")
    class Meta:
        template = 'blocks/contact_form_block.html'
        icon = 'mail'
        label = 'Kontaktformular'

class VideoBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    video = EmbedBlock()
    caption = blocks.TextBlock(required=False)
    class Meta:
        template = 'blocks/video_block.html'
        icon = 'media'
        label = 'Video'

class QuoteBlock(blocks.StructBlock):
    quote_text = blocks.TextBlock(required=True)
    author = blocks.CharBlock(required=True)
    author_title = blocks.CharBlock(required=False)
    author_company = blocks.CharBlock(required=False)
    author_image = ImageChooserBlock(required=False)
    class Meta:
        template = 'blocks/quote_block.html'
        icon = 'openquote'
        label = 'Zitat'

class StatsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    stats = blocks.ListBlock(
        blocks.StructBlock([
            ('number', blocks.CharBlock(required=True)),
            ('label', blocks.CharBlock(required=True)),
            ('icon_class', blocks.CharBlock(required=False)),
        ])
    )

    class Meta:
        template = 'blocks/stats_block.html'
        icon = 'list-ol'
        label = 'Statistiken'

# Layout Wrappers

class TwoColumnLayout(blocks.StructBlock):
    left = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('cards', CardBlock()),
        ('video', VideoBlock()),
        ('quote', QuoteBlock()),
        ('contact_form', ContactFormBlock()),
        ('html', blocks.RawHTMLBlock()),
    ], blank=True, use_json_field=True)
    right = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('cards', CardBlock()),
        ('video', VideoBlock()),
        ('quote', QuoteBlock()),
        ('contact_form', ContactFormBlock()),
        ('html', blocks.RawHTMLBlock()),
    ], blank=True, use_json_field=True)
    left_width = blocks.ChoiceBlock(choices=[('3','25%'), ('4','33%'), ('5','42%'), ('6','50%')], default='6')
    class Meta:
        template = 'layout/two_column_layout.html'
        icon = 'grip'
        label = 'Two Column Layout'

class ThreeColumnLayout(blocks.StructBlock):
    left = StreamField([...], blank=True, use_json_field=True)  # ähnlich wie oben
    center = StreamField([...], blank=True, use_json_field=True)
    right = StreamField([...], blank=True, use_json_field=True)
    class Meta:
        template = 'layout/three_column_layout.html'
        icon = 'grip'
        label = 'Three Column Layout'

class HeroContentLayout(blocks.StructBlock):
    hero = StreamField([...], blank=True, use_json_field=True)
    content = StreamField([...], blank=True, use_json_field=True)
    class Meta:
        template = 'layout/hero_content_layout.html'
        icon = 'image'
        label = 'Hero Content Layout'

# ähnliche für SidebarLayout, GridLayout, etc...

class ContentPage(Page):
    """Flexible Content-Seite mit verschiedenen Layouts"""
    
    layout_choice = models.CharField(
        max_length=50,
        choices=[
            ('hero_content', 'Hero + Content'),
            ('two_column', 'Zweispaltig'),
            ('three_column', 'Dreispaltig'),
            ('sidebar', 'Sidebar + Content'),
            ('grid', 'Grid-Layout'),
            ('asymmetric_grid', 'Asymmetrisches Grid'),
            ('timeline', 'Timeline'),
            ('parallax_section', 'Parallax-Sektion'),
        ],
        default='hero_content',
        help_text="Wählen Sie das Layout für diese Seite"
    )
    
    intro_text = RichTextField(blank=True, help_text="Einführungstext (optional)")
    
    # StreamFields für verschiedene Layout-Bereiche
    hero_content = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('video', VideoBlock()),
        ('html', blocks.RawHTMLBlock(icon='code', label='HTML Code')),
    ], blank=True, use_json_field=True, help_text="Hero-Bereich (für Hero-Layout)")
    
    main_content = StreamField([
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
    ], blank=True, use_json_field=True, help_text="Haupt-Content")
    
    # Für Two-Column Layout
    left_column = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('cards', CardBlock()),
        ('quote', QuoteBlock()),
        ('html', blocks.RawHTMLBlock(icon='code', label='HTML Code')),
    ], blank=True, use_json_field=True, help_text="Linke Spalte")
    
    right_column = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('cards', CardBlock()),
        ('quote', QuoteBlock()),
        ('html', blocks.RawHTMLBlock(icon='code', label='HTML Code')),
    ], blank=True, use_json_field=True, help_text="Rechte Spalte")
    
    # Für Three-Column Layout  
    column_1 = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('cards', CardBlock()),
    ], blank=True, use_json_field=True, help_text="Spalte 1")
    
    column_2 = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('cards', CardBlock()),
    ], blank=True, use_json_field=True, help_text="Spalte 2")
    
    column_3 = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('cards', CardBlock()),
    ], blank=True, use_json_field=True, help_text="Spalte 3")
    
    # Für Sidebar Layout
    sidebar_content = StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full', label='Text')),
        ('image', ImageChooserBlock(icon='image', label='Bild')),
        ('cards', CardBlock()),
        ('contact_form', ContactFormBlock()),
    ], blank=True, use_json_field=True, help_text="Sidebar-Inhalt")
    
    # Für Timeline Layout
    timeline_items = StreamField([
        ('timeline_item', blocks.StructBlock([
            ('date', blocks.CharBlock(required=True, help_text="Datum/Jahr")),
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
        ])),
    ], blank=True, use_json_field=True, help_text="Timeline-Einträge")
    
    content_panels = Page.content_panels + [
        FieldPanel('layout_choice'),
        FieldPanel('intro_text'),
        MultiFieldPanel([
            FieldPanel('hero_content'),
        ], heading="Hero-Bereich (für Hero-Layout)"),
        FieldPanel('main_content'),
        MultiFieldPanel([
            FieldPanel('left_column'),
            FieldPanel('right_column'),
        ], heading="Zwei-Spalten Layout"),
        MultiFieldPanel([
            FieldPanel('column_1'),
            FieldPanel('column_2'), 
            FieldPanel('column_3'),
        ], heading="Drei-Spalten Layout"),
        MultiFieldPanel([
            FieldPanel('sidebar_content'),
        ], heading="Sidebar Layout"),
        MultiFieldPanel([
            FieldPanel('timeline_items'),
        ], heading="Timeline Layout"),
    ]
    
    class Meta:
        verbose_name = "Content-Seite mit Layouts"
        verbose_name_plural = "Content-Seiten mit Layouts"
