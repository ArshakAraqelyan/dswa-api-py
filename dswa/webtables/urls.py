from django.urls import path

from .views import WebtableBeautifulSoup

urlpatterns = [
    path('api/v2/scrap/webtables', WebtableBeautifulSoup.as_view())
]