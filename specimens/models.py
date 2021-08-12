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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True,
        help_text='Select the specimen\'s order')
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True,
        help_text='Select the specimen\'s family')
    subfamily = models.ForeignKey(Subfamily, on_delete=models.CASCADE, null=True, blank=True,
        help_text='Select the specimen\'s subfamily')
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE, null=True, blank=True,
        help_text='Select the specimen\'s tribe')
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, null=True, blank=True,
        help_text='Select the specimen\'s genus')
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=True, blank=True,
        help_text='Select the specimen\'s species')
    subspecies = models.ForeignKey(Subspecies, on_delete=models.CASCADE, null=True, blank=True,
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
    determiner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='determiners',
        help_text='Select the person who determined the specimen')
    determined_year = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX, default='U',
        help_text='Select the specimen\'s sex')
    stage = models.CharField(max_length=10, choices=STAGE, default='adult',
        help_text='Select the specimen\'s stage')
    preparer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='preparers',
        help_text='Select the person who prepared the specimen')
    preparation = models.CharField(max_length=15, choices=PREPARATION_TYPE, default='spread',
        help_text='Select the specimen\'s preparation type')
    preparation_date = models.DateField(null=True, blank=True, help_text='Enter the preparation date')
    labels_printed = models.BooleanField(help_text='Are labels printed for the specimen?')
    labeled = models.BooleanField(help_text='Is the specimen labeled?')
    photographed = models.BooleanField(help_text='Is the specimen photographed?')
    identified = models.BooleanField(help_text='Is the specimen identified to at least species?')
