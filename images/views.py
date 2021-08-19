from rest_framework import viewsets
from images.models import InsectImage, PlantImage, HabitatImage
from images.serializers import *

class InsectImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InsectImage.objects.all()
    serializer_class = InsectImageSerializer

class PlantImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer

class HabitatImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HabitatImage.objects.all()
    serializer_class = HabitatImageSerializer
