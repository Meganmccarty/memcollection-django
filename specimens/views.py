from django.shortcuts import render
from rest_framework import generics, permissions
from specimens.models import *
from specimens.serializers import *

class SpecimenRecordList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SpecimenRecord.objects.all()
    serializer_class = SpecimenRecordSerializer
