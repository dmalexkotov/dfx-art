from django.db import models
from django.http import Http404
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, RichTextFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from common.blocks import ContactBlock

@register_setting
class SiteSettings(BaseSetting):
    contacts = StreamField([
        ('contact', ContactBlock())
    ])
    email = models.CharField(max_length=60, help_text='Add email')
    privacy_text = RichTextField(null=True, blank=True, help_text='Privacy text')
    
    panels = [
        StreamFieldPanel('contacts'),
        RichTextFieldPanel('privacy_text'),
        FieldPanel('email')
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