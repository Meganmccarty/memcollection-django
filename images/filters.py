from django_filters import rest_framework as filters
from images.models import *

class InsectImageFilter(filters.FilterSet):
    species = filters.CharFilter(field_name='species__name', lookup_expr='icontains')
    country = filters.CharFilter(field_name='country__name', lookup_expr='icontains')
    state = filters.CharFilter(field_name='state__name', lookup_expr='icontains')
    county = filters.CharFilter(field_name='county__name', lookup_expr='icontains')
    locality = filters.CharFilter(field_name='locality__name', lookup_expr='icontains')
    gps_lat = filters.CharFilter(field_name='gps__latitude', lookup_expr='icontains')
    gps_long = filters.CharFilter(field_name='gps__longitude', lookup_expr='icontains')
    elevation = filters.CharFilter(field_name='gps__elevation', lookup_expr='icontains')
    collecting_trip = filters.CharFilter(field_name='collecting_trip__name', lookup_expr='icontains')
    
    class Meta:
        model = InsectImage
        fields = [
            'id',
            'name',
            'caption',
            'alt_text',
            'date',
            'other_notes',
            'species',
            'identified',
            'sex',
            'stage',
            'status',
            'country',
            'state',
            'county',
            'locality',
            'gps_lat',
            'gps_long',
            'elevation',
            'collecting_trip'
        ]

class PlantImageFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='country__name', lookup_expr='icontains')
    state = filters.CharFilter(field_name='state__name', lookup_expr='icontains')
    county = filters.CharFilter(field_name='county__name', lookup_expr='icontains')
    locality = filters.CharFilter(field_name='locality__name', lookup_expr='icontains')
    gps_lat = filters.CharFilter(field_name='gps__latitude', lookup_expr='icontains')
    gps_long = filters.CharFilter(field_name='gps__longitude', lookup_expr='icontains')
    elevation = filters.CharFilter(field_name='gps__elevation', lookup_expr='icontains')
    collecting_trip = filters.CharFilter(field_name='collecting_trip__name', lookup_expr='icontains')
    
    class Meta:
        model = PlantImage
        fields = [
            'id',
            'name',
            'caption',
            'alt_text',
            'date',
            'other_notes',
            'latin_name',
            'common_name',
            'country',
            'state',
            'county',
            'locality',
            'gps_lat',
            'gps_long',
            'elevation',
            'collecting_trip'
        ]

class HabitatImageFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='country__name', lookup_expr='icontains')
    state = filters.CharFilter(field_name='state__name', lookup_expr='icontains')
    county = filters.CharFilter(field_name='county__name', lookup_expr='icontains')
    locality = filters.CharFilter(field_name='locality__name', lookup_expr='icontains')
    gps_lat = filters.CharFilter(field_name='gps__latitude', lookup_expr='icontains')
    gps_long = filters.CharFilter(field_name='gps__longitude', lookup_expr='icontains')
    elevation = filters.CharFilter(field_name='gps__elevation', lookup_expr='icontains')
    collecting_trip = filters.CharFilter(field_name='collecting_trip__name', lookup_expr='icontains')
    
    class Meta:
        model = HabitatImage
        fields = [
            'id',
            'name',
            'caption',
            'alt_text',
            'date',
            'other_notes',
            'country',
            'state',
            'county',
            'locality',
            'gps_lat',
            'gps_long',
            'elevation',
            'collecting_trip'
        ]