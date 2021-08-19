from django_filters import rest_framework as filters
from taxonomy.models import *

class OrderFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['name', 'common_name']

class FamilyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')

    class Meta:
        model = Family
        fields = ['name', 'common_name']

class SubfamilyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')

    class Meta:
        model = Subfamily
        fields = ['name', 'common_name']

class TribeFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')

    class Meta:
        model = Tribe
        fields = ['name', 'common_name']
    
class GenusFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')

    class Meta:
        model = Genus
        fields = ['name', 'common_name']

class SpeciesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')
    mona = filters.CharFilter(field_name='mona', lookup_expr='icontains')
    p3 = filters.CharFilter(field_name='p3', lookup_expr='icontains')

    class Meta:
        model = Species
        fields = ['name', 'common_name', 'mona', 'p3']

class SubspeciesFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    common_name = filters.CharFilter(field_name='common_name', lookup_expr='icontains')
    mona = filters.CharFilter(field_name='mona', lookup_expr='icontains')
    p3 = filters.CharFilter(field_name='p3', lookup_expr='icontains')

    class Meta:
        model = Subspecies
        fields = ['name', 'common_name', 'mona', 'p3']