from django.contrib import admin
from taxonomy.models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'authority')
    fields = ('name', 'common_name', 'authority')

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'authority', 'order')
    fields = ('order', 'name', 'common_name', 'authority')

@admin.register(Subfamily)
class SubfamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'authority', 'family')
    fields = ('family', 'name', 'common_name', 'authority')

@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'authority', 'subfamily')
    fields = ('subfamily', 'name', 'common_name', 'authority')

@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ('name', 'common_name', 'authority', 'tribe')
    fields = ('tribe', 'name', 'common_name', 'authority')

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('get_binomial', 'common_name', 'authority', 'mona', 'p3')
    fields = ('genus', 'name', 'common_name', 'authority', 'mona', 'p3')

@admin.register(Subspecies)
class SubspeciesAdmin(admin.ModelAdmin):
    list_display = ('get_trinomial', 'common_name', 'authority', 'mona', 'p3')
    fields = ('species', 'name', 'common_name', 'authority', 'mona', 'p3')