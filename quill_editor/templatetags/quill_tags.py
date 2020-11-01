import json
from django import template
from delta import html
from django.utils.safestring import mark_safe
from wagtail.core.rich_text import RichText

register = template.Library()


@register.filter()
def quillrichtext(value):
    quill_delta_string = value
    if isinstance(value, RichText):
        quill_delta_string = value.source
    delta_object = json.loads(quill_delta_string)
    return mark_safe(html.render(delta_object['ops']))
