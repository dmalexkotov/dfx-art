from django import template

from portfolio.models import PorfolioPage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_portfolio_pages(context):
    return PorfolioPage.objects.all()
