from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from specimens.models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']
    fields = ('first_name', 'middle_initial', 'last_name', 'suffix')

@admin.register(SpecimenRecord)
class SpecimenRecordAdmin(admin.ModelAdmin):
    list_display = (
        'usi', 'order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies',
        'determiner', 'determined_year', 'sex', 'stage', 'preparer', 'preparation', 'preparation_date',
        'labels_printed', 'labeled', 'photographed', 'identified',
        'collecting_trip', 'country', 'state', 'county', 'locality', 'gps', 'collected_date',
        'display_collectors', 'method', 'weather', 'temp_F', 'time_of_day', 'get_habitat', 'notes'
    )
    
    list_editable = (
        'determined_year', 'sex', 'stage', 'preparation', 'preparation_date',
        'labels_printed', 'labeled', 'photographed', 'identified'
    )

    list_filter = ('labels_printed', 'labeled', 'photographed', 'identified')

    search_fields = ('usi',)

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

    @admin.display(description='Habitat')
    def get_habitat(self, obj):
        return format_html('{}',
            mark_safe(obj.habitat)
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
