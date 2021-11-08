from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from images.models import InsectImage, PlantImage, HabitatImage
from images.filters import *
from images.serializers import *

class InsectImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InsectImage.objects.select_related('species', 'country', 'state', 'county', 'locality', 'gps')
    serializer_class = InsectImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InsectImageFilter

class PlantImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlantImage.objects.select_related('country', 'state', 'county', 'locality', 'gps')
    serializer_class = PlantImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantImageFilter

class HabitatImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HabitatImage.objects.select_related('country', 'state', 'county', 'locality', 'gps')
    serializer_class = HabitatImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HabitatImageFilter
