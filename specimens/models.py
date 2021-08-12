from django.db import models
from geography.models import *
from taxonomy.models import *

class Person(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter the person\'s first name')
    middle_initial = models.CharField(max_length=1, blank=True,
        help_text='Enter the person\'s middle initial')
    last_name = models.CharField(max_length=50, help_text='Enter the person\'s last name')
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
        return f'{self.first_name} {self.get_middle_initial()} {self.last_name}{self.get_suffix()}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class SpecimenRecord(models.Model):
    # MEM number
    usi = models.CharField(max_length=15, verbose_name='Unique Specimen Identifier',
        help_text='Enter the specimen\'s unique identifier number')
    
    # Taxonomy fields
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s order')
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s family')
    subfamily = models.ForeignKey(Subfamily, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s subfamily')
    tribe = models.ForeignKey(Tribe, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s tribe')
    genus = models.ForeignKey(Genus, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s genus')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s species')
    subspecies = models.ForeignKey(Subspecies, on_delete=models.SET_NULL, null=True, blank=True,
        help_text='Select the specimen\'s subspecies')
    
    # Specimen details
    SEX = (
        ('M', 'male'),
        ('F', 'female'),
        ('U', 'unknown'),
    )
    STAGE = (
        ('egg', 'egg'),
        ('larva', 'larva'),
        ('nymph', 'nymph'),
        ('pupa', 'pupa'),
        ('adult', 'adult'),
    )
    PREPARATION_TYPE = (
        ('spread', 'spread'),
        ('pinned', 'pinned'),
        ('minuten', 'minuten'),
        ('pointed', 'pointed'),
        ('envelope.', 'envelope'),
        ('container', 'container'),
        ('alcohol', 'alcohol'),
    )

    # Specimen fields
    determiner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='specimen_determiners',
        help_text='Select the person who determined the specimen')
    determined_year = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX, default='U',
        help_text='Select the specimen\'s sex')
    stage = models.CharField(max_length=10, choices=STAGE, default='adult',
        help_text='Select the specimen\'s stage')
    preparer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='specimen_preparers',
        help_text='Select the person who prepared the specimen')
    preparation = models.CharField(max_length=15, choices=PREPARATION_TYPE, default='spread',
        help_text='Select the specimen\'s preparation type')
    preparation_date = models.DateField(null=True, blank=True, help_text='Enter the preparation date')
    labels_printed = models.BooleanField(help_text='Are labels printed for the specimen?')
    labeled = models.BooleanField(help_text='Is the specimen labeled?')
    photographed = models.BooleanField(help_text='Is the specimen photographed?')
    identified = models.BooleanField(help_text='Is the specimen identified to at least species?')

    # Geography fields
    collecting_trip = models.ForeignKey(CollectingTrip, on_delete=models.SET_NULL, related_name='specimens',
        null=True, blank=True, help_text='Select the collecting trip during which the specimen was collected')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='specimens',
        null=True, blank=True, help_text='Select the country in which the specimen was collected')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, related_name='specimens',
        null=True, blank=True, help_text='Select the state in which the specimen was collected')
    county = models.ForeignKey(County, on_delete=models.SET_NULL, related_name='specimens',
        null=True, blank=True, help_text='Select the county in which the specimen was collected')
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, related_name='specimens',
        null=True, blank=True, help_text='Select the locality at which the specimen was collected')
    gps = models.ForeignKey(GPS, on_delete=models.SET_NULL, related_name='specimens',
        null=True, blank=True, help_text='Select the GPS coordinates at which the specimen was collected')
    
    # Other fields
    MONTH = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    METHOD = (
        ('net', 'net'),
        ('reared', 'reared'),
        ('trap', 'trap'),
        ('UV trap', 'UV trap'),
        ('light', 'light'),
        ('MV light', 'MV light'),
        ('MV light sheet', 'MV light sheet'),
        ('UV light', 'UV light'),
        ('UV light sheet', 'UV light sheet'),
        ('UV/MV light sheet', 'UV/MV light sheet'),
        ('bait', 'bait'),
        ('by hand', 'by hand'),
        ('sweep', 'sweep'),
    )

    day = models.IntegerField(null=True, blank=True,
        help_text='Enter the day the specimen was collected, if known')
    month = models.CharField(max_length=10, choices=MONTH, null=True, blank=True,
        help_text='Select the month the specimen was collected, if known')
    year = models.IntegerField(null=True, blank=True,
        help_text='Enter the year the specimen was collected, if known')
    method = models.CharField(max_length=20, null=True, blank=True,
        help_text='Select the method used to collected the specimen')
    weather = models.CharField(max_length=100, null=True, blank=True,
        help_text='Enter the weather conditions during the specimen\'s collection')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True,
        help_text='Enter the temperature (F) during the specimen\'s collection if outdoors')
    time_of_day = models.CharField(max_length=50, null=True, blank=True,
        help_text='Enter the approximate time of the specimen\'s collection')
    habitat = models.TextField(null=True, blank=True,
        help_text='Enter habitat details where the specimen was collected')
    notes = models.TextField(null=True, blank=True, help_text='Enter any other notes about the specimen')