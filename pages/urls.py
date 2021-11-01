from django.urls import path
from django.conf.urls import include
from django.views.decorators.cache import cache_page
from rest_framework import routers
from pages.views import *

router = routers.DefaultRouter()
router.register(r'species-pages', SpeciesPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('species-pages', cache_page(60 * 15)(SpeciesPageViewSet))
]