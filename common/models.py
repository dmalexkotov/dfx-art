from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    StreamFieldPanel, RichTextFieldPanel, FieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Rendition
from wagtail.contrib.settings.models import BaseSetting, register_setting

from common.blocks import ContactBlock


@register_setting
class SiteSettings(BaseSetting):
    contacts = StreamField([
        ('contact', ContactBlock())
    ])
    email = models.CharField(max_length=60, help_text='Add email')

    watermark_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Watermark logo'),
    )

    watermark_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Watermark backgroud'),
    )

    privacy_text = RichTextField(null=True, blank=True, help_text='Privacy text')

    panels = [
        StreamFieldPanel('contacts'),
        RichTextFieldPanel('privacy_text'),
        FieldPanel('email'),
        ImageChooserPanel('watermark_logo'),
        ImageChooserPanel('watermark_background'),
    ]


class EmptyPage(Page):
    """Страницы заглушка."""
    def serve(self, request):
        raise Http404()


class PrivacyPage(Page):
    """Страницы заглушка."""
    max_count = 1

    content = RichTextField()

    content_panels = Page.content_panels + [
        RichTextFieldPanel('content')
    ]


@receiver(post_save, sender=SiteSettings)
def delete_all_image_rendition(**kwargs):
    Rendition.objects.all().delete()
