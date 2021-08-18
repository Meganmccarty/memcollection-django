from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from taxonomy.models import *
from taxonomy.serializers import *

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name']

class FamilyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name']

class SubfamilyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subfamily.objects.all()
    serializer_class = SubfamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name']

class TribeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name']

class GenusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name']

class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name', 'mona', 'p3']

class SubspeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subspecies.objects.all()
    serializer_class = SubspeciesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'common_name', 'mona', 'p3']
