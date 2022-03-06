from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic.base import RedirectView

from .conf import settings
from .viewsets import HomepageViewSet


CACHE_TIMEOUT = 30


urlpatterns = [
    path(
        r'<str:language>/',
        cache_page(CACHE_TIMEOUT)(HomepageViewSet.as_view()),
        name=settings.URLNAME_HOMEPAGE
    ),
    path(
        r'',
        cache_page(CACHE_TIMEOUT)(HomepageViewSet.as_view()),
        name=settings.URLNAME_HOMEPAGE
    ),
]
