from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url
from rest_framework.decorators import action
from wagtail.api.v2.views import BaseAPIViewSet

from portfolio.models import PorfolioPage

class PortfolioAPIEndpoint(BaseAPIViewSet):
    model = PorfolioPage

    def projects_html_view(self, request, pk=None):
        portfolio_page = get_object_or_404(PorfolioPage, pk=pk)
        projects = list(portfolio_page.projects)
        is_last_page = False
        page = int(request.GET.get('page') or 0)
        page_size = int(request.GET.get('size') or settings.PORTFOLIO_PAGE_SIZE)
        if page and page > 0:
            is_last_page = len(projects) <= (page - 1) * page_size + page_size
            projects = projects[(page - 1) * page_size: (page - 1) * page_size + page_size]
        return render(request, 'portfolio/projects_ajax.html', {
            'projects': projects
        }, status= 211 if is_last_page else 200)

    @classmethod
    def get_urlpatterns(cls):
        """
        This returns a list of URL patterns for the endpoint
        """
        urls = super().get_urlpatterns()
        urls += [
            url(
                r'^(?P<pk>\d+)/projects-ajax/$',
                cls.as_view({'get': 'projects_html_view'}),
                name='projects_html_view'
            ),
        ]
        return urls