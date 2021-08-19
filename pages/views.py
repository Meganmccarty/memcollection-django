from rest_framework import viewsets
from pages.models import SpeciesPage
from pages.serializers import SpeciesPageSerializer

class SpeciesPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpeciesPage.objects.all()
    serializer_class = SpeciesPageSerializer