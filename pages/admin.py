from django.contrib import admin
from pages.models import *

@admin.register(SpeciesPage)
class SpeciesPage(admin.ModelAdmin):
    list_display = ['get_binomial', 'display_refs']

@admin.register(Reference)
class Reference(admin.ModelAdmin):
    list_display = ['citation']

