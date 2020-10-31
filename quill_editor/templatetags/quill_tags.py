import json
from django import template
from delta import html
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def quillrichtext(quill_delta_string):
    delta_object = json.loads(quill_delta_string)
    return mark_safe(html.render(delta_object['ops']))
