from django.db import models
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from common.blocks import ContactBlock

@register_setting
class ContactsSettings(BaseSetting):
    contacts = StreamField([
        ('contact', ContactBlock())
    ])
    email = models.CharField(max_length=60, help_text='Add email')
    
    panels = [
        StreamFieldPanel('contacts'),
    ]


class EmptyPage(Page):
    """Страницы заглушка."""
