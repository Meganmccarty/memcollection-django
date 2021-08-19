from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from geography.models import *
from geography.filters import *
from geography.serializers import *

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter

class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StateFilter

class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountyFilter

class LocalityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LocalityFilter

class GPSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GPSFilter

class CollectingTripViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CollectingTrip.objects.all()
    serializer_class = CollectingTripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CollectingTripFilter