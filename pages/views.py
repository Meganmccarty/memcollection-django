from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from pages.models import SpeciesPage
from pages.filters import SpeciesPageFilter
from pages.serializers import SpeciesPageSerializer

class SpeciesPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpeciesPage.objects.select_related(
        'species', 'species__genus', 'species__genus__tribe', 'species__genus__tribe__subfamily',
        'species__genus__tribe__subfamily__family', 'species__genus__tribe__subfamily__family__order'
        ).prefetch_related('species__subspecies', 'insect_images', 'insect_images__species',
        'habitat_images', 'plant_images', 'references')
    serializer_class = SpeciesPageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpeciesPageFilter