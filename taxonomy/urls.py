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
router.register(r'nested-families', NestedFamilyViewSet)
router.register(r'nested-subfamilies', NestedSubfamilyViewSet)

urlpatterns = router.urls