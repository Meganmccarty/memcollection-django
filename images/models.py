from django.db import models
from geography.models import *
from taxonomy.models import Species
from pages.models import SpeciesPage

class BaseImage(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a short title for the image')
    caption = models.TextField(help_text='Enter a caption for the image')
    alt_text = models.TextField(help_text='Enter alternative text for the image')
    date = models.DateField(help_text='Enter the date the image was taken')
    other_notes = models.TextField(blank=True, help_text='Enter any other notes about this image')

    class Meta:
        abstract = True

class InsectImage(BaseImage):
    image = models.FileField(upload_to='insect-photos')
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=True, blank=True,
        related_name='insect_images', help_text='Select the species in the image, if it is identified')
    species_page = models.ForeignKey(SpeciesPage, on_delete=models.CASCADE, null=True, blank=True,
        related_name='insect_images', help_text='Select the species page this images belongs to, if it is identified')
    identified = models.BooleanField(help_text='Check this box if the insect in the image has been identified')
    
    SEX = (
        ('male', 'male'),
        ('female', 'female'),
        ('unknown', 'unknown'),
    )
    STAGE = (
        ('egg', 'egg'),
        ('larva', 'larva'),
        ('nymph', 'nymph'),
        ('pupa', 'pupa'),
        ('adult', 'adult'),
    )
    STATUS = (
        ('wild', 'wild'),
        ('reared', 'reared'),
        ('bred', 'bred'),
    )
    
    sex = models.CharField(max_length=10, choices=SEX, default='unknown',
        help_text='Select the sex of the insect in the image')
    stage = models.CharField(max_length=10, choices=STAGE, default='adult',
        help_text='Select the stage of the insect in the image')
    status = models.CharField(max_length=10, choices=STATUS, default='wild',
        help_text='Select the status of the insect in the image')
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='insect_images',
        null=True, blank=True, help_text='Select the country in which the image was taken')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='insect_images',
        null=True, blank=True, help_text='Select the state in which the image was taken')
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='insect_images',
        null=True, blank=True, help_text='Select the county in which the image was taken')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='insect_images',
        null=True, blank=True, help_text='Select the locality at which the image was taken')
    gps = models.ForeignKey(GPS, on_delete=models.CASCADE, related_name='insect_images',
        null=True, blank=True, help_text='Select the GPS coordinates at which the image was taken')
    collecting_trip = models.ForeignKey(CollectingTrip, on_delete=models.CASCADE, related_name='insect_images',
        null=True, blank=True, help_text='Select the collecting trip during which the image was taken')

    class Meta:
        ordering = ['name']
    
    def get_image_url(self):
        image = self.image
        return f'{image.url}'

    def __str__(self):
        return f'{self.name}'
    
class PlantImage(BaseImage):
    image = models.FileField(upload_to='plant-photos')
    species_page = models.ManyToManyField(SpeciesPage, related_name='plant_images',
        help_text='Select the species pages(s) to which this plant image should belong')
    latin_name = models.CharField(max_length=100, blank=True,
        help_text='Enter the scientific name of the plant, if known')
    common_name = models.CharField(max_length=100, blank=True,
        help_text='Enter the common name of the plant, if known')
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='plant_images',
        null=True, blank=True, help_text='Select the country in which the image was taken')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='plant_images',
        null=True, blank=True, help_text='Select the state in which the image was taken')
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='plant_images',
        null=True, blank=True, help_text='Select the county in which the image was taken')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='plant_images',
        null=True, blank=True, help_text='Select the locality at which the image was taken')
    gps = models.ForeignKey(GPS, on_delete=models.CASCADE, related_name='plant_images',
        null=True, blank=True, help_text='Select the GPS coordinates at which the image was taken')
    collecting_trip = models.ForeignKey(CollectingTrip, on_delete=models.CASCADE, related_name='plant_images',
        null=True, blank=True, help_text='Select the collecting trip during which the image was taken')
    
    class Meta:
        ordering = ['name']
    
    def get_image_url(self):
        image = self.image
        return f'{image.url}'
    
    def __str__(self):
        return f'{self.name}'

class HabitatImage(BaseImage):
    image = models.FileField(upload_to='habitat-photos')
    species_page = models.ManyToManyField(SpeciesPage, related_name='habitat_images',
        help_text='Select the species page(s) to which this habitat image should belong')
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='habitat_images',
        null=True, blank=True, help_text='Select the country in which the image was taken')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='habitat_images',
        null=True, blank=True, help_text='Select the state in which the image was taken')
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='habitat_images',
        null=True, blank=True, help_text='Select the county in which the image was taken')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='habitat_images',
        null=True, blank=True, help_text='Select the locality at which the image was taken')
    gps = models.ForeignKey(GPS, on_delete=models.CASCADE, related_name='habitat_images',
        null=True, blank=True, help_text='Select the GPS coordinates at which the image was taken')
    collecting_trip = models.ForeignKey(CollectingTrip, on_delete=models.CASCADE, related_name='habitat_images',
        null=True, blank=True, help_text='Select the collecting trip during which the image was taken')

    class Meta:
        ordering = ['name']
    
    def get_image_url(self):
        image = self.image
        return f'{image.url}'
    
    def __str__(self):
        return f'{self.name}'