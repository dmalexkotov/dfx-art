from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class PortfolioProject(blocks.StructBlock):
    cover = ImageChooserBlock(required=False)


class PortfolioPageBlock(PortfolioProject):
    project_page = blocks.PageChooserBlock(required=True)

    class Meta:
        template = 'portfolio/blocks/portfolio_game_block.html'
        icon = 'plus'
        label = 'Portfolio Page block'


class PortfolioVideoBlock(PortfolioProject):
    video = DocumentChooserBlock(required=True)

    class Meta:
        template = 'portfolio/blocks/portfolio_animation_block.html'
        icon = 'plus'
        label = 'Portfolio Video block'


class PortfolioImageBlock(PortfolioProject):
    image = ImageChooserBlock(required=True)

    class Meta:
        template = 'portfolio/blocks/portfolio_drawing_block.html'
        icon = 'plus'
        label = 'Portfolio Image block'
