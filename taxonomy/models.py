from django.db import models

class TaxonomyBaseInfo(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the scientific name')
    common_name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the common name')
    authority = models.CharField(max_length=100, help_text='Enter the authority')

    class Meta:
        abstract = True
        ordering = ['name']

class Order(TaxonomyBaseInfo):

    def __str__(self):
        return f'{self.name}'

class Family(TaxonomyBaseInfo):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
        help_text='Select the order to which this family belongs')
    
    class Meta:
        verbose_name_plural = 'Families'

    def __str__(self):
        return f'{self.name}'

class Subfamily(TaxonomyBaseInfo):
    family = models.ForeignKey(Family, on_delete=models.CASCADE,
        help_text='Select the family to which this subfamily belongs')
    
    class Meta:
        verbose_name_plural = 'Subfamilies'
    
    def __str__(self):
        return f'{self.name}'

class Tribe(TaxonomyBaseInfo):
    subfamily = models.ForeignKey(Subfamily, on_delete=models.CASCADE,
        help_text='Select the subfamily to which this tribe belongs')
    
    def __str__(self):
        return f'{self.name}'

class Genus(TaxonomyBaseInfo):
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE,
        help_text='Select the tribe to which this genus belongs')
    
    class Meta:
        verbose_name_plural = 'Genera'
    
    def __str__(self):
        return f'{self.name}'

class Species(TaxonomyBaseInfo):
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE,
        help_text='Select the genus to which this species belongs')
    mona = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,
        help_text='Enter the MONA (Hodges) # for the species (Lepidoptera only)')
    p3 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,
        help_text='Enter the P3 (Pohl, Patterson, Pelham 2016) # for the species (Lepidoptera only)')
    
    class Meta:
        verbose_name_plural = 'Species'
    
    def __str__(self):
        return f'{self.name}'

class Subspecies(TaxonomyBaseInfo):
    species = models.ForeignKey(Species, on_delete=models.CASCADE,
        help_text='Select the species to which this subspecies belongs')
    mona = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,
        help_text='Enter the MONA (Hodges) # for the subspecies (Lepidoptera only). ' \
        'If it lacks its own MONA #, use the nominate species\' #')
    p3 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,
        help_text='Enter the P3 (Pohl, Patterson, Pelham 2016) # for the subspecies (Lepidoptera only). ' \
        'If it lacks its own P3 #, use the nominate species\' #')
    
    class Meta:
        verbose_name_plural = 'Subspecies'
    
    def __str__(self):
        return f'{self.name}'