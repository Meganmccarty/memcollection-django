from django.contrib import admin
from specimens.models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    fields = ('first_name', 'middle_initial', 'last_name', 'suffix')

# Register your models here.
