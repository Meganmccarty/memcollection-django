from django.shortcuts import render
from rest_framework import generics, permissions
from geography.models import *
from geography.serializers import *

class CountryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CountyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = County.objects.all()
    serializer_class = CountySerializer

class LocalityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

class GPSList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer

class CollectingTripList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CollectingTrip.objects.all()
    serializer_class = CollectingTripSerializer