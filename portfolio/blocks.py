from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class PortfolioProject(blocks.StructBlock):
    cover = ImageChooserBlock(
        required=False, help_text='The image sould be about 300x500 size')


class PortfolioPageBlock(PortfolioProject):
    project_page = blocks.PageChooserBlock(required=True)

    class Meta:
        template = 'portfolio/blocks/portfolio_page_block.html'
        icon = 'plus'
        label = 'Portfolio Page block'


class PortfolioVideoBlock(PortfolioProject):
    title = blocks.CharBlock(required=False)
    video = DocumentChooserBlock(required=True)

    class Meta:
        template = 'portfolio/blocks/portfolio_video_block.html'
        icon = 'plus'
        label = 'Portfolio Video block'


class PortfolioImageBlock(PortfolioProject):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=True)

    class Meta:
        template = 'portfolio/blocks/portfolio_image_block.html'
        icon = 'plus'
        label = 'Portfolio Image block'
