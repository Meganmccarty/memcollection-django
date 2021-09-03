from django_filters import rest_framework as filters
from geography.models import *

class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    abbr = filters.CharFilter(field_name='abbr', lookup_expr='icontains')

    class Meta:
        model = Country
        fields = ['name', 'abbr']

class StateFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    abbr = filters.CharFilter(field_name='abbr', lookup_expr='icontains')

    class Meta:
        model = State
        fields = ['name', 'abbr']

class CountyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = County
        fields = ['name']

class LocalityFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    range = filters.CharFilter(field_name='range', lookup_expr='icontains')
    town = filters.CharFilter(field_name='town', lookup_expr='icontains')

    gps_lat = filters.CharFilter(field_name='places_collected__latitude', lookup_expr='icontains')
    gps_long = filters.CharFilter(field_name='places_collected__longitude', lookup_expr='icontains')
    elevation = filters.CharFilter(field_name='places_collected__elevation', lookup_expr='icontains')

    class Meta:
        model = Locality
        fields = ['name', 'range', 'town']

class GPSFilter(filters.FilterSet):
    locality = filters.CharFilter(field_name='locality__name', lookup_expr='icontains')
    gps_lat = filters.CharFilter(field_name='latitude', lookup_expr='icontains')
    gps_long = filters.CharFilter(field_name='longitude', lookup_expr='icontains')
    elevation = filters.CharFilter(field_name='elevation', lookup_expr='icontains')

    class Meta:
        model = GPS
        fields = ['locality', 'gps_lat', 'gps_long', 'elevation']

class CollectingTripFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    slug = filters.CharFilter(field_name='slug', lookup_expr='icontains')
    start_date = filters.DateFilter(field_name='start_date', lookup_expr='icontains')
    end_date = filters.DateFilter(field_name='end_date', lookup_expr='icontains')
    notes = filters.CharFilter(field_name='notes', lookup_expr='icontains')

    class Meta:
        model = CollectingTrip
        fields = ['name', 'slug', 'start_date', 'end_date', 'notes']