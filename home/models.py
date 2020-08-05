from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from home.blocks import (
    AboutItemBlock, AboutListBlock, MainBlock,
    ProjectListBlock, InformersBlock, ProgrammingBlock,
    FoundersPatentsBlock, AwardsBlock, HistoryBlock
)


class HomePage(Page):
    """Главная страница."""

    content = StreamField([
        ('main', MainBlock()),
        ('about', AboutItemBlock()),
        ('about_list', AboutListBlock()),
        ('projects_list', ProjectListBlock()),
        ('informers', InformersBlock()),
        ('programming', ProgrammingBlock()),
        ('awargs', AwardsBlock()),
        ('founders_patents', FoundersPatentsBlock()),
        ('history', HistoryBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]
