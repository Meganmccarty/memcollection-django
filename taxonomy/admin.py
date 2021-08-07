from django.contrib import admin
from taxonomy.models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'authority')
    fields = ('name', 'common_name', 'authority')

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'common_name', 'authority')
    fields = ('order', 'name', 'common_name', 'authority')

@admin.register(Subfamily)
class SubfamilyAdmin(admin.ModelAdmin):
    list_display = ('family', 'name', 'common_name', 'authority')
    fields = ('family', 'name', 'common_name', 'authority')

@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ('subfamily', 'name', 'common_name', 'authority')
    fields = ('subfamily', 'name', 'common_name', 'authority')

@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ('tribe', 'name', 'common_name', 'authority')
    fields = ('tribe', 'name', 'common_name', 'authority')

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('genus', 'name', 'common_name', 'authority', 'mona', 'p3')
    fields = ('genus', 'name', 'common_name', 'authority', 'mona', 'p3')

@admin.register(Subspecies)
class SubspeciesAdmin(admin.ModelAdmin):
    list_display = ('species', 'name', 'common_name', 'authority', 'mona', 'p3')
    fields = ('species', 'name', 'common_name', 'authority', 'mona', 'p3')