from django.shortcuts import render
from rest_framework import generics, permissions
from taxonomy.models import *
from taxonomy.serializers import *

# Create your views here.

class OrderList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FamilyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class SubfamilyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subfamily.objects.all()
    serializer_class = SubfamilySerializer

class TribeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer

class GenusList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer

class SpeciesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class SubspeciesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subspecies.objects.all()
    serializer_class = SubspeciesSerializer
