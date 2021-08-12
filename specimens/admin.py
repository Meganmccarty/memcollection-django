from django.contrib import admin
from specimens.models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    fields = ('first_name', 'middle_initial', 'last_name', 'suffix')

@admin.register(SpecimenRecord)
class SpecimenRecordAdmin(admin.ModelAdmin):
    list_display = ('usi', 'species', 'locality', 'year', 'display_collectors', 'temp_C', 'temp_F')
    fieldsets = (
        ('Specimen Details', {
            'fields': [
                'usi', ('order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies'),
                ('determiner', 'determined_year'), ('sex', 'stage'), ('preparer', 'preparation', 'preparation_date'),
                ('labels_printed', 'labeled', 'photographed', 'identified')
            ]
        }),
        ('Locality Details', {
            'fields': [
                'collecting_trip', ('country', 'state', 'county', 'locality', 'gps'), ('day', 'month', 'year'),
                'collector', 'method', ('weather', 'temperature', 'time_of_day'), 'habitat', 'notes'
            ]
        }),
    )
