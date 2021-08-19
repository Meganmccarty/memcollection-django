from rest_framework import routers
from geography.views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'counties', CountyViewSet)
router.register(r'localities', LocalityViewSet)
router.register(r'gps-coordinates', GPSViewSet)
router.register(r'collecting-trips', CollectingTripViewSet)

urlpatterns = router.urls