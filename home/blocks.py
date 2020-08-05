from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class MainBlock(blocks.StructBlock):
    """Блок для баннера на главной странице."""

    title = blocks.CharBlock(required=True, help_text=_('Add title'))
    text = blocks.TextBlock(required=True, help_text=_('Add text'))
    background = DocumentChooserBlock(
        required=True, help_text=_('Add background image or video'))

    class Meta:
        template = 'home/blocks/main_block.html'
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
    """Абстрактный Блок с заголовком."""

    title = blocks.CharBlock(required=True, help_text=_('Add title'))


class AboutItemBlock(HeaderedBlock):
    """Блока описания."""
    title = blocks.CharBlock(required=True, help_text=_('Add title'))
    sub_title = blocks.CharBlock(required=False, help_text=_('Add subtitle'))
    text = blocks.RichTextBlock(required=True, help_text=_('Add text'))
    video_background = DocumentChooserBlock(
        required=False, help_text=_('Add background video'))
    image_background = ImageChooserBlock(
        required=False, help_text=_('Add background image'))
    side = blocks.BooleanBlock(required=False, help_text=_('Flip side'))

    class Meta:
        template = 'home/blocks/about_block.html'
        icon = 'edit'
        label = 'About block'


class AboutListBlock(HeaderedBlock):
    """Набор блоков описания."""

    items = blocks.ListBlock(AboutItemBlock())

    class Meta:
        template = 'home/blocks/about_list_block.html'
        icon = 'edit'
        label = 'About list block'


class ProjectListBlock(HeaderedBlock):
    """Блок со списком проектов для главной."""

    content = blocks.ListBlock(
        blocks.PageChooserBlock(page_type='portfolio.projectpage'))

    class Meta:
        template = 'home/blocks/project_list_block.html'
        icon = 'edit'
        label = 'Project list block'


class ProgrammingBlock(HeaderedBlock):
    """Блок про программирование."""

    description = blocks.RichTextBlock(
        required=False, help_text=_('Description'))
    items = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock()),
        ('description', blocks.TextBlock())
    ]))

    class Meta:
        template = 'home/blocks/programming_block.html'
        icon = 'edit'
        label = 'Programming block'


class AwardsBlock(HeaderedBlock):
    """Блок с наградами."""

    items = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock()),
        ('badge', ImageChooserBlock()),
        ('title', blocks.CharBlock()),
        ('description', blocks.TextBlock())
    ]))

    class Meta:
        template = 'home/blocks/awards_block.html'
        icon = 'edit'
        label = 'Awards block'


class FoundersPatentsBlock(HeaderedBlock):
    """Блок с патентом."""

    items = blocks.ListBlock(blocks.StructBlock([
        ('desc_title', blocks.CharBlock()),
        ('title', blocks.CharBlock()),
        ('description', blocks.TextBlock()),
        ('image', ImageChooserBlock()),
        ('image_text', blocks.CharBlock()),
    ]))

    class Meta:
        template = 'home/blocks/founder_patents_block.html'
        icon = 'edit'
        label = 'Founder patents block'


class HistoryBlock(HeaderedBlock):
    """Блок с историей компании."""

    content = blocks.RichTextBlock()

    class Meta:
        template = 'home/blocks/history_block.html'
        icon = 'edit'
        label = 'History block'
