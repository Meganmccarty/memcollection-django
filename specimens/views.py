from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from specimens.models import SpecimenRecord, SpecimenRecordImage
from specimens.filters import *
from specimens.serializers import *

class SpecimenRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpecimenRecord.objects.select_related(
        # 'order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies',
        'collecting_trip', 'country', 'state', 'county', 'locality', 'gps',
        'determiner', 'preparer').prefetch_related('collecting_trip__states', 'collector', 'specimen_images').all()
    serializer_class = SpecimenRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpecimenRecordFilter

class SpecimenRecordImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpecimenRecordImage.objects.all()
    serializer_class = SpecimenRecordImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpecimenRecordImageFilter
