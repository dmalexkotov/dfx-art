from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel
)
from wagtail.core import fields
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from portfolio.blocks import (
    PortfolioPageBlock, PortfolioImageBlock, PortfolioVideoBlock
)


class ProjectPage(Page):
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Ad cover'),
    )

    video = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Ad video')
    )
    description = fields.RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover'),
        DocumentChooserPanel('video'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label='Gallery images'),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        page = context['page']
        context['prev_page'] = page.get_prev_siblings().live().first()
        context['next_page'] = page.get_next_siblings().live().first()
        return context


class ProjectGalleryImage(Orderable):
    page = ParentalKey(
        ProjectPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    video = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.CASCADE,
        related_name='+',
        null=True
    )

    panels = [
        ImageChooserPanel('image'),
        DocumentChooserPanel('video'),
    ]


class PorfolioPage(Page):
    projects = fields.StreamField([
        ('page_block', PortfolioPageBlock()),
        ('image_block', PortfolioImageBlock()),
        ('video_block', PortfolioVideoBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('projects')
    ]

    def get_pagination_info(self, request, items_count):
        page = int(request.GET.get("page") or 1)
        page_size = int(request.GET.get("size") or settings.PORTFOLIO_PAGE_SIZE)
        
        pages_count = (
            int(items_count / page_size)
            + (items_count % page_size and 1 or 0)
        )
        return {
            'item_from': (page - 1) * page_size,
            'item_to': (page - 1) * page_size + page_size,
            'pages_total': pages_count,
            'pages_total_range': range(pages_count),
            'current_page': page,
            'page_size': page_size
        }

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context['pagination'] = self.get_pagination_info(
            request, len(context['page'].projects)
        )
        # Get all posts
        # all_posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        # # Paginate all posts by 2 per page
        # paginator = Paginator(all_posts, 2)
        # # Try to get the ?page=x value
        # page = request.GET.get("page")
        # try:
        #     # If the page exists and the ?page=x is an int
        #     posts = paginator.page(page)
        # except PageNotAnInteger:
        #     # If the ?page=x is not an int; show the first page
        #     posts = paginator.page(1)
        # except EmptyPage:
        #     # If the ?page=x is out of range (too high most likely)
        #     # Then return the last page
        #     posts = paginator.page(paginator.num_pages)

        # # "posts" will have child pages; you'll need to use .specific in the template
        # # in order to access child properties, such as youtube_video_id and subtitle
        # context["posts"] = posts
        return context
