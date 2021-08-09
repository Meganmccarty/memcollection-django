from django.db import models
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
        if self.state == 'Alaska':
            return f'{self.name} Bor.'
        elif self.state == 'Louisiana':
            return f'{self.name} Par.'
        else:
            return f'{self.name} Co.'
    
    def __str__(self):
        return f'{self.name}'

class Locality(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
        related_name='localities', help_text='Select the locality\'s country')
    state = models.ForeignKey(State, on_delete=models.CASCADE,
        related_name='states', help_text='Select the locality\'s state')
    county = models.ForeignKey(County, on_delete=models.CASCADE,
        related_name='counties', help_text='Select the locality\'s county')
    name = models.CharField(max_length=100, help_text='Enter the locality\'s name')
    range = models.CharField(max_length=10,
        help_text='Enter the distance and direction of this locality from the nearest town')
    town = models.CharField(max_length=50, help_text='Enter the nearest town')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Localities'
    
    def __str__(self):
        return f'{self.name}'

class GPS(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE,
        related_name='GPS_coordinates', help_text='Select the locality for this set of coordinates')
    latitude = models.DecimalField(max_digits=13, decimal_places=10, help_text='Enter the latitude')
    longitude = models.DecimalField(max_digits=13, decimal_places=10, help_text='Enter the longitude')
    elevation = models.DecimalField(max_digits=6, decimal_places=2, help_text='Enter the elevation in meters')

    class Meta:
        ordering = ['latitude', 'longitude']
        verbose_name_plural = 'GPS coordinates'
    
    def __str__(self):
        return f'{self.latitude} {self.longitude}'

class CollectingTrip(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the trip')
    states = models.ManyToManyField(State)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'