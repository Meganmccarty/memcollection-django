from django.contrib import admin
from geography.models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr')
    fields = ('name', 'abbr')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr', 'country')
    fields = ('country', 'name', 'abbr')

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('county_abbr', 'state')
    fields = ('state', 'name')

@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'range', 'town', 'county', 'state', 'country')
    fields = ('country', 'state', 'county', 'name', 'range', 'town')

@admin.register(GPS)
class GPSAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'locality', 'normalize_elevation')
    fields = ('locality', 'latitude', 'longitude', 'elevation')

@admin.register(CollectingTrip)
class CollectingTripAdmin(admin.ModelAdmin):
    list_display = ('name', 'states_collected', 'start_date', 'end_date', 'notes')
    fields = ('name', 'states', 'start_date', 'end_date', 'notes')