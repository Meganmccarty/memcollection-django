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
    list_display = ('name', 'range', 'town', 'content_type')
    fields = ('content_type', 'object_id', 'name', 'range', 'town')

@admin.register(GPS)
class GPSAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'locality', 'elevation_and_meters')
    fields = ('locality', 'latitude', 'longitude', 'elevation')

@admin.register(CollectingTrip)
class CollectingTripAdmin(admin.ModelAdmin):
    list_display = ('name', 'states_collected', 'start_date', 'end_date', 'notes')
    fields = ('name', 'states', 'start_date', 'end_date', 'notes')