from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    """Блок для баннера на главной странице."""

    title = blocks.CharBlock(required=True, help_text=_('Add title'))
    text = blocks.TextBlock(required=True, help_text=_('Add text'))
    background = DocumentChooserBlock(
        required=True, help_text=_('Add background image or video'))

    class Meta:
        template = 'home/blocks/banner_block.html'
        icon = 'edit'
        label = 'Banner block'


class InformersBlock(blocks.StructBlock):
    """Блок для блока описания на главной странице."""

    content = blocks.ListBlock(blocks.StructBlock([
        ('text',  blocks.TextBlock(required=True, help_text=_('Add text'))),
        (
            'image',
            ImageChooserBlock(
                required=True, help_text=_('Add background image')
            )
        )
    ]))

    class Meta:
        template = 'home/blocks/informers_block.html'
        icon = 'edit'
        label = 'Informers Block'


class HeaderedBlock(blocks.StructBlock):
    """Блок с заголовком."""

    title = blocks.CharBlock(required=True, help_text=_('Add title'))


class AboutBlock(HeaderedBlock):
    """Блок для блока описания на главной странице."""

    content = blocks.ListBlock(blocks.StructBlock([
        ('title', blocks.CharBlock(required=True, help_text=_('Add title'))),
        ('text',  blocks.TextBlock(required=True, help_text=_('Add text'))),
        (
            'image',
            ImageChooserBlock(
                required=True, help_text=_('Add background image')
            )
        )
    ]))

    class Meta:
        template = 'home/blocks/about_block.html'
        icon = 'edit'
        label = 'About block'


class ProjectListBlock(HeaderedBlock):
    """Блок со списком проектов для главной."""

    content = blocks.ListBlock(
        blocks.PageChooserBlock(page_type='portfolio.projectpage'))

    class Meta:
        template = 'home/blocks/project_list_block.html'
        icon = 'edit'
        label = 'Project list block'
