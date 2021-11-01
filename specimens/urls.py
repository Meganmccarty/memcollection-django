from django.urls import path
from django.conf.urls import include
from django.views.decorators.cache import cache_page
from rest_framework import routers
from specimens.views import *

router = routers.DefaultRouter()
router.register(r'specimen-records', SpecimenRecordViewSet)
router.register(r'specimen-record-images', SpecimenRecordImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('specimen-records', cache_page(60 * 15)(SpecimenRecordViewSet))
]