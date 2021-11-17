from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from serpy import serializer
from taxonomy.models import *
from taxonomy.filters import *
from taxonomy.serializers import *

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

class FamilyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FamilyFilter

class SubfamilyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subfamily.objects.all()
    serializer_class = SubfamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubfamilyFilter

class TribeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TribeFilter

class GenusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenusFilter

class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpeciesFilter

class SubspeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subspecies.objects.all()
    serializer_class = SubspeciesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubspeciesFilter

class NestedFamilyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Family.objects.select_related('order')
    serializer_class = NestedFamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NestedFamilyFilter

class NestedSubfamilyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subfamily.objects.select_related('family', 'family__order')
    serializer_class = NestedSubfamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NestedSubfamilyFilter