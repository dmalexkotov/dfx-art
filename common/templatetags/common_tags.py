import mimetypes
from django import template

register = template.Library()


@register.simple_tag()
def get_mime_type(file_path):
    mimme_type_object = mimetypes.guess_type(file_path)
    mime_type_str = (
        mimme_type_object[0]
        if (len(mimme_type_object))
        else ''
    )
    return mime_type_str
