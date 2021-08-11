from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import DecimalField

class Country(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the name of the country')
    abbr = models.CharField(max_length=10, help_text='Enter the country\'s abbreviation')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return f'{self.name}'

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
        related_name='states', help_text='Select the state\'s country')
    name = models.CharField(max_length=50, help_text='Enter the name of the state')
    abbr = models.CharField(max_length=10, help_text='Enter the state\'s abbrevation')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'

class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE,
        related_name='counties', help_text='Select the county\'s state')
    name = models.CharField(max_length=50, help_text='Enter the name of the county')
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Counties'
    
    def county_abbr(self):
        if self.state.name == 'Alaska':
            return f'{self.name} Bor.'
        elif self.state.name == 'Louisiana':
            return f'{self.name} Par.'
        else:
            return f'{self.name} Co.'
    
    def __str__(self):
        return f'{self.name}'

class Locality(models.Model):
    content_type = models.ForeignKey(ContentType, limit_choices_to={
        'model__in': (
            'country',
            'state',
            'county')
        }, on_delete=models.CASCADE, default='')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=100, help_text='Enter the locality\'s name')
    range = models.CharField(max_length=10, blank=True,
        help_text='Enter the distance and direction of this locality from the nearest town')
    town = models.CharField(max_length=50, blank=True, help_text='Enter the nearest town')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Localities'
    
    def range_and_town(self):
        if self.range:
            return f'{self.range} {self.town}'
        else:
            return f'{self.town}'

    def __str__(self):
        return f'{self.name}'

class GPS(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE,
        related_name='places_collected', help_text='Select the locality for this set of coordinates')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, help_text='Enter the latitude')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, help_text='Enter the longitude')
    elevation = models.DecimalField(max_digits=6, decimal_places=2, help_text='Enter the elevation in meters')

    class Meta:
        ordering = ['latitude', 'longitude']
        verbose_name_plural = 'GPS coordinates'
    
    def normalize_latitude(self):
        return self.latitude.normalize()
    
    def normalize_longitude(self):
        return self.longitude.normalize()

    def normalize_elevation(self):
        return self.elevation.normalize()

    def elevation_and_meters(self):
        return f'{self.elevation}m'

    def __str__(self):
        return f'{self.normalize_latitude()} {self.normalize_longitude()}'

class CollectingTrip(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the trip')
    states = models.ManyToManyField(State, related_name='collecting_trips')
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
    
    @property
    def states_collected(self):
        return ', '.join([str(state) for state in self.states.all()])
    
    def __str__(self):
        return f'{self.name}'