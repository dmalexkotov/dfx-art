from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField


from home.blocks import AboutBlock, BannerBlock, ProjectListBlock


class HomePage(Page):

    content = StreamField([
        ('banner', BannerBlock()),
        ('about', AboutBlock()),
        ('project_list', ProjectListBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]
