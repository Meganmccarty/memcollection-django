from rest_framework import routers
from specimens.views import *

router = routers.DefaultRouter()
router.register(r'specimen-records', SpecimenRecordViewSet)
router.register(r'specimen-record-images', SpecimenRecordImageViewSet)

urlpatterns = router.urls