from django.contrib import admin
from images.models import InsectImage, PlantImage, HabitatImage

@admin.register(InsectImage)
class InsectImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = [
        'image', 'name', 'caption', 'alt_text', 'datetime', 'other_notes', 'species', 'species_page',
        'identified', 'sex', 'stage', 'status', 'country', 'state', 'county', 'locality', 'gps', 'collecting_trip'
    ]

@admin.register(PlantImage)
class PlantImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = [
        'image', 'name', 'caption', 'alt_text', 'datetime', 'other_notes', 'species_page', 'latin_name',
        'common_name', 'country', 'state', 'county', 'locality', 'gps', 'collecting_trip'
    ]

@admin.register(HabitatImage)
class HabitatImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = [
        'image', 'name', 'caption', 'alt_text', 'datetime', 'other_notes', 'species_page',
        'country', 'state', 'county', 'locality', 'gps', 'collecting_trip'
    ]

