from django.contrib import admin
from pages.models import *

@admin.register(SpeciesPage)
class SpeciesPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_refs']

    def get_queryset(self, request):
        qs = super(SpeciesPageAdmin, self).get_queryset(request)
        return qs.prefetch_related('references')

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['citation']

