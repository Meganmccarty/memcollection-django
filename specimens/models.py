from django.db import models
from geography.models import *
from taxonomy.models import *

class Person(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter the person\'s first name')
    middle_initial = models.CharField(max_length=1, blank=True,
        help_text='Enter the person\'s middle initial')
    last_name = models.CharField(max_length=1, help_text='Enter the person\'s last name')
    suffix = models.CharField(max_length=5, blank=True,
        help_text='Enter a suffix, if the person has one')
    
    class Meta:
        ordering = ['last_name']
        verbose_name_plural = 'People'

    def get_middle_initial(self):
        return f'{self.middle_initial}.' if self.middle_initial else ''
    
    def get_suffix(self):
        return f', {self.suffix}' if self.suffix else ''

    def full_name(self):
        return f'{self.first_name} {self.get_middle_initial} {self.last_name}{self.get_suffix}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
