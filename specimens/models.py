import datetime
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from ckeditor.fields import RichTextField
from geography.models import *
from taxonomy.models import *

class Person(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter the person\'s first name')
    middle_initial = models.CharField(default='', max_length=1, blank=True,
        help_text='Enter the person\'s middle initial')
    last_name = models.CharField(max_length=50, help_text='Enter the person\'s last name')
    suffix = models.CharField(default='', max_length=5, blank=True,
        help_text='Enter a suffix, if the person has one')
    
    class Meta:
        ordering = ['last_name']
        verbose_name_plural = 'People'

    def get_middle_initial(self):
        return f' {self.middle_initial}.' if self.middle_initial else ''
    
    def get_suffix(self):
        return f', {self.suffix}' if self.suffix else ''

    def collector_name(self):
        first_initial = self.first_name[0]
        return f'{first_initial}. {self.last_name}{self.get_suffix()}'

    def __str__(self):
        return f'{self.first_name}{self.get_middle_initial()} {self.last_name}{self.get_suffix()}'

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
    order_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    family_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    subfamily_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    tribe_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    genus_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    species_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    subspecies_json = models.JSONField(default=dict, encoder=DjangoJSONEncoder)
    
    # Specimen details
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
    PREPARATION_TYPE = (
        ('spread', 'spread'),
        ('pinned', 'pinned'),
        ('minuten', 'minuten'),
        ('pointed', 'pointed'),
        ('envelope', 'envelope'),
        ('container', 'container'),
        ('alcohol', 'alcohol'),
    )

    # Specimen fields
    determiner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='specimen_determiners',
        null=True, blank=True, help_text='Select the person who determined the specimen')
    determined_year = models.IntegerField(null=True, blank=True, help_text='Enter the year the determination was made')
    sex = models.CharField(max_length=10, null=True, choices=SEX, default='unknown',
        help_text='Select the specimen\'s sex')
    stage = models.CharField(max_length=10, null=True, choices=STAGE, default='adult',
        help_text='Select the specimen\'s stage')
    preparer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='specimen_preparers',
        null=True, help_text='Select the person who prepared the specimen')
    preparation = models.CharField(null=True, max_length=15, choices=PREPARATION_TYPE, default='spread',
        help_text='Select the specimen\'s preparation type')
    preparation_date = models.DateField(null=True, blank=True, help_text='Enter the preparation date')
    labels_printed = models.BooleanField(null=True, help_text='Are labels printed for the specimen?')
    labeled = models.BooleanField(null=True, help_text='Is the specimen labeled?')
    photographed = models.BooleanField(null=True, help_text='Is the specimen photographed?')
    identified = models.BooleanField(null=True, help_text='Is the specimen identified to at least species?')

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
        ('Net', 'Net'),
        ('Reared', 'Reared'),
        ('Trap', 'Trap'),
        ('UV trap', 'UV trap'),
        ('Light', 'Light'),
        ('MV light', 'MV light'),
        ('MV light sheet', 'MV light sheet'),
        ('UV light', 'UV light'),
        ('UV light sheet', 'UV light sheet'),
        ('UV/MV light sheet', 'UV/MV light sheet'),
        ('UV/MV/LED light sheet', 'UV/MV/LED light sheet'),
        ('Bait', 'Bait'),
        ('By hand', 'By hand'),
        ('Sweep', 'Sweep'),
    )

    day = models.IntegerField(null=True, blank=True,
        help_text='Enter the day the specimen was collected, if known')
    month = models.CharField(max_length=10, choices=MONTH, null=True, blank=True,
        help_text='Select the month the specimen was collected, if known')
    year = models.IntegerField(null=True, blank=True,
        help_text='Enter the year the specimen was collected, if known')
    collected_date = models.CharField(max_length=30, blank=True)
    full_date = models.CharField(max_length=30, blank=True)
    num_date = models.CharField(max_length=30, blank=True)
    collector = models.ManyToManyField(Person, verbose_name='Collector(s)', related_name='specimen_collectors',
        help_text='Select the specimen\'s collector(s)')
    method = models.CharField(max_length=50, choices=METHOD, null=True, blank=True,
        help_text='Select the method used to collected the specimen')
    weather = models.CharField(max_length=100, null=True, blank=True,
        help_text='Enter the weather conditions during the specimen\'s collection')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True,
        help_text='Enter the temperature (F) during the specimen\'s collection if outdoors')
    temp_F = models.CharField(default='', max_length=10, blank=True)
    temp_C = models.CharField(default='', max_length=10, blank=True)
    time_of_day = models.CharField(max_length=50, null=True, blank=True,
        help_text='Enter the approximate time of the specimen\'s collection')
    habitat = RichTextField(null=True, blank=True,
        help_text='Enter habitat details where the specimen was collected')
    notes = RichTextField(null=True, blank=True, help_text='Enter any other notes about the specimen')

    class Meta:
        ordering = ['usi']
    
    def convert_to_json(self):
        if self.order:
            self.order_json = {
                "name": self.order.name,
                "authority": self.order.authority,
                "common_name": self.order.common_name
            }

        if self.family:
            self.family_json = {
                "name": self.family.name,
                "authority": self.family.authority,
                "common_name": self.family.common_name
            }
        
        if self.subfamily:
            self.subfamily_json = {
                "name": self.subfamily.name,
                "authority": self.subfamily.authority,
                "common_name": self.subfamily.common_name
            }
        
        if self.tribe:
            self.tribe_json = {
                "name": self.tribe.name,
                "authority": self.tribe.authority,
                "common_name": self.tribe.common_name
            }
        
        if self.genus:
            self.genus_json = {
                "name": self.genus.name,
                "authority": self.genus.authority,
                "common_name": self.genus.common_name
            }
        
        if self.species:
            self.species_json = {
                "name": self.species.name,
                "authority": self.species.authority,
                "common_name": self.species.common_name,
                "mona": self.species.mona,
                "p3": self.species.p3
            }
        
        if self.subspecies:
            self.subspecies_json = {
                "name": self.subspecies.name,
                "authority": self.subspecies.authority,
                "common_name": self.subspecies.common_name,
                "mona": self.subspecies.mona,
                "p3": self.subspecies.p3
            }

    def taxon(self):
        if self.subspecies:
            return {
                "name": f'{self.genus_json["name"]} {self.species_json["name"]} {self.subspecies_json["name"]}',
                "authority": f'{self.subspecies_json["authority"]}',
                "common_name": f'{self.subspecies_json["common_name"]}',
                "mona": self.subspecies_json["mona"],
                "p3": self.subspecies_json["p3"]
            }
        elif self.species:
            return {
                "name": f'{self.genus_json["name"]} {self.species_json["name"]}',
                "authority": f'{self.species_json["authority"]}',
                "common_name": f'{self.species_json["common_name"]}',
                "mona": self.species_json["mona"],
                "p3": self.species_json["p3"]
            }
        elif self.genus:
            return {
                "name": f'{self.genus_json["name"]}',
                "authority": f'{self.genus_json["authority"]}',
                "common_name": f'{self.genus_json["common_name"]}'
            }
        elif self.tribe:
            return {
                "name": f'{self.tribe_json["name"]}',
                "authority": f'{self.tribe_json["authority"]}',
                "common_name": f'{self.tribe_json["common_name"]}'
            }
        elif self.subfamily:
            return {
                "name": f'{self.subfamily_json["name"]}',
                "authority": f'{self.subfamily_json["authority"]}',
                "common_name": f'{self.subfamily_json["common_name"]}'
            }
        elif self.family:
            return {
                "name": f'{self.family_json["name"]}',
                "authority": f'{self.family_json["authority"]}',
                "common_name": f'{self.family_json["common_name"]}'
            }
        elif self.order:
            return {
                "name": f'{self.order_json["name"]}',
                "authority": f'{self.order_json["authority"]}',
                "common_name": f'{self.order_json["common_name"]}'
            }
        else:
            return ''
    
    def get_collected_date(self):
        if self.day:
            return f'{self.day}-{self.month[0:3]}-{self.year}'
        elif self.month:
            return f'{self.month} {self.year}'
        else:
            return f'{self.year}'
    
    def get_full_date(self):
        if self.day:
            return f'{self.day} {self.month} {self.year}'
        elif self.month:
            return f'{self.month} {self.year}'
        else:
            return f'{self.year}'
    
    def get_num_date(self):
        month = self.month

        if month:
            datetime_object = datetime.datetime.strptime(month, "%B")
            if datetime_object.month < 10:
                month = f'0{datetime_object.month}'
            else:
                month = datetime_object.month

        if self.day:
            if self.day < 10:
                return f'{self.year}-{month}-0{self.day}'
            else:
                return f'{self.year}-{month}-{self.day}'
        elif month:
            return f'{self.year}-{month}'
        else:
            return f'{self.year}'

    def display_collectors(self):
        return ', '.join([str(collector.collector_name()) for collector in self.collector.all()])
    
    def display_preparer(self):
        if self.preparer:
            return f'{self.preparer.first_name} {self.preparer.last_name}{self.preparer.get_suffix()}'
        else:
            return ''
    
    def display_determiner(self):
        if self.determiner:
            return f'{self.determiner.first_name} {self.determiner.last_name}{self.determiner.get_suffix()}'
        else:
            return ''

    DEGREE_SIGN= u'\N{DEGREE SIGN}'
    def get_temp_F(self):
        if self.temperature:
            return f'{round(self.temperature, 1)}{self.DEGREE_SIGN}F'
        else:
            return ''

    def get_temp_C(self):
        if self.temperature:
            celsius = (self.temperature - 32) * 5/9
            return f'{round(celsius, 1)}{self.DEGREE_SIGN}C'
        else:
            return ''

    def __str__(self):
        return f'{self.usi}'
    
    def save(self, *args, **kwargs):
        self.convert_to_json()
        self.collected_date = self.get_collected_date()
        self.full_date = self.get_full_date()
        self.num_date = self.get_num_date()
        self.temp_F = self.get_temp_F()
        self.temp_C = self.get_temp_C()
        super(SpecimenRecord, self).save(*args, **kwargs)

class SpecimenRecordImage(models.Model):
    image = models.FileField(upload_to='specimen-photos')
    usi = models.ForeignKey(SpecimenRecord, on_delete=models.CASCADE,
        related_name='specimen_images', help_text='Select the specimen in the image')
    
    POSITION = (
        ('dorsal', 'dorsal'),
        ('ventral', 'ventral'),
        ('lateral', 'lateral'),
    )

    position = models.CharField(max_length=10, choices=POSITION, default='dorsal',
        help_text='Select the view of the specimen in the image')
    date = models.DateField(help_text='Enter the date the image was taken')

    def get_image_url(self):
        image = self.image
        return f'{image.url}'

    def __str__(self):
        return f'{self.usi}'