from rest_framework import routers
from taxonomy.views import *

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'families', FamilyViewSet)
router.register(r'subfamilies', SubfamilyViewSet)
router.register(r'tribes', TribeViewSet)
router.register(r'genera', GenusViewSet)
router.register(r'species', SpeciesViewSet)
router.register(r'subspecies', SubspeciesViewSet)

urlpatterns = router.urls