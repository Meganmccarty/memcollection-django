from rest_framework import routers
from images.views import *

router = routers.DefaultRouter()
router.register(r'insect-images', InsectImageViewSet)
router.register(r'plant-images', PlantImageViewSet)
router.register(r'habitat-images', HabitatImageViewSet)

urlpatterns = router.urls