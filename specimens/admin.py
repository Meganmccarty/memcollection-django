from django.contrib import admin
from specimens.models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
    fields = ('first_name', 'middle_initial', 'last_name', 'suffix')

@admin.register(SpecimenRecord)
class SpecimenRecordAdmin(admin.ModelAdmin):
    list_display = ('usi', 'order', 'family', 'genus', 'species', 'sex', 'stage', 'preparation', 'method', 'collecting_trip', 'country', 'state', 'county',
        'locality', 'collected_date', 'display_collectors')
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

    def get_queryset(self, request):
        qs = super(SpecimenRecordAdmin, self).get_queryset(request)
        return qs.select_related(
            'order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies',
            'collecting_trip', 'country', 'state', 'county', 'locality', 'gps',
            'determiner', 'preparer').prefetch_related('collector', 'specimen_images')

@admin.register(SpecimenRecordImage)
class SpecimenRecordImageAdmin(admin.ModelAdmin):
    list_display = ('usi', 'image')
