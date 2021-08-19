from rest_framework import routers
from pages.views import *

router = routers.DefaultRouter()
router.register(r'species-pages', SpeciesPageViewSet)

urlpatterns = router.urls