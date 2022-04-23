from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify

class Country(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the name of the country')
    abbr = models.CharField(max_length=10, help_text='Enter the country\'s abbreviation')
    localities = GenericRelation('Locality')

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
    localities = GenericRelation('Locality')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'

class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE,
        related_name='counties', help_text='Select the county\'s state')
    name = models.CharField(max_length=50, help_text='Enter the name of the county')
    county_abbr = models.CharField(default='', max_length=50)
    localities = GenericRelation('Locality')
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Counties'

    def __str__(self):
        return f'{self.name}'
    
    def render_county_abbr(self):
        if self.state.name == 'Alaska' and 'Census' not in self.name:
            return f'{self.name} Boro.'
        elif self.state.name == 'Alaska' and 'Census' in self.name:
            return f'{self.name}'
        elif self.state.name == 'Louisiana':
            return f'{self.name} Par.'
        else:
            return f'{self.name} Co.'

    def save(self, *args, **kwargs):
        self.county_abbr = self.render_county_abbr()
        super(County, self).save(*args, **kwargs)

class Locality(models.Model):
    content_type = models.ForeignKey(ContentType, limit_choices_to={
        'model__in': (
            'country',
            'state',
            'county')
        }, on_delete=models.CASCADE, default='')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=100, default='', help_text='Enter the locality\'s name', blank=True)
    range = models.CharField(max_length=10, default='', blank=True,
        help_text='Enter the distance and direction of this locality from the nearest town')
    town = models.CharField(max_length=50, default='', blank=True, help_text='Enter the nearest town')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Localities'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'--, {self.range} {self.town}'

class GPS(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE,
        related_name='places_collected', help_text='Select the locality for this set of coordinates')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True,
        blank=True, help_text='Enter the latitude')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True,
        blank=True, help_text='Enter the longitude')
    elevation = models.CharField(max_length=15, help_text='Enter the elevation in meters')

    class Meta:
        ordering = ['latitude', 'longitude']
        verbose_name_plural = 'GPS coordinates'
    
    def normalize_latitude(self):
        if self.latitude:
            return self.latitude.normalize()
    
    def normalize_longitude(self):
        if self.longitude:
            return self.longitude.normalize()

    def elevation_and_meters(self):
        if self.elevation:
            return f'{self.elevation}m'

    def __str__(self):
        return f'{self.normalize_latitude()} {self.normalize_longitude()}'

class CollectingTrip(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the trip')
    states = models.ManyToManyField(State, related_name='collecting_trips')
    slug = models.SlugField(default='', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = RichTextField(null=True, blank=True)

    class Meta:
        ordering = ['name']
    
    def states_collected(self):
        return ', '.join([str(state) for state in self.states.all()])
    
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CollectingTrip, self).save(*args, **kwargs)