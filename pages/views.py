from rest_framework import generics, permissions
from pages.models import SpeciesPage
from pages.serializers import SpeciesPageSerializer

class SpeciesPageList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SpeciesPage.objects.all()
    serializer_class = SpeciesPageSerializer