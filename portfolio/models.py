from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel
)
from wagtail.core import fields
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from portfolio.blocks import (
    PortfolioPageBlock, PortfolioImageBlock, PortfolioVideoBlock
)


class ProjectPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Ad cover'),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover'),
    ]

    class Meta:
        abstract = True


class GameProjectPage(ProjectPage):
    video = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Ad video')
    )
    description = fields.RichTextField(null=True, blank=True)

    content_panels = ProjectPage.content_panels + [
        DocumentChooserPanel('video'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label='Gallery images'),
    ]


class GameProjectGalleryImage(Orderable):
    page = ParentalKey(
        GameProjectPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]


class SketchProjectPage(ProjectPage):
    description = fields.RichTextField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    content_panels = ProjectPage.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('description'),
    ]


class DrawingProjectPage(ProjectPage):
    description = fields.RichTextField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    content_panels = ProjectPage.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('description'),
    ]


class AnimationProjectPage(ProjectPage):
    video = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Ad video')
    )

    content_panels = ProjectPage.content_panels + [
        DocumentChooserPanel('video'),
    ]


class PorfolioPage(Page):
    projects = fields.StreamField([
        ('page_block', PortfolioPageBlock()),
        ('image_block', PortfolioImageBlock()),
        ('video_block', PortfolioVideoBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('projects')
    ]
