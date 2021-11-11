from django_filters import rest_framework as filters
from pages.models import SpeciesPage

class SpeciesPageFilter(filters.FilterSet):
    order = filters.CharFilter(field_name='species__genus__tribe__subfamily__family__order__name',
        label='Order', lookup_expr='icontains')
    family = filters.CharFilter(field_name='species__genus__tribe__subfamily__family__name',
        label='Family', lookup_expr='icontains')
    subfamily = filters.CharFilter(field_name='species__genus__tribe__subfamily__name', label='Subfamily',
        lookup_expr='icontains')
    tribe = filters.CharFilter(field_name='species__genus__tribe__name', label='Tribe', lookup_expr='icontains')
    genus = filters.CharFilter(field_name='species__genus__name', label='Genus', lookup_expr='icontains')
    species = filters.CharFilter(field_name='species__name', label='Species', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', label='Title', lookup_expr='icontains')

    class Meta:
        model = SpeciesPage
        fields = [
            'order',
            'family',
            'subfamily',
            'tribe',
            'genus',
            'species',
            'title'
        ]