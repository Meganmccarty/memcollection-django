from django.contrib import admin
from pages.models import *

@admin.register(SpeciesPage)
class SpeciesPage(admin.ModelAdmin):
    list_display = ['species', 'description']

@admin.register(Reference)
class Reference(admin.ModelAdmin):
    list_display = ['citation']

