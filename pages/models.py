from django.db import models
from ckeditor.fields import RichTextField
from taxonomy.models import Species

class SpeciesPage(models.Model):
    species = models.OneToOneField(Species, on_delete=models.SET_NULL, null=True,
        related_name='species_page', help_text='Select the species for this page')
    taxonomy = RichTextField(null=True, blank=True, help_text='Enter taxonomy details')
    description = RichTextField(null=True, blank=True, help_text='Enter species description')
    distribution = RichTextField(null=True, blank=True, help_text='Enter distribution details')
    seasonality = RichTextField(null=True, blank=True, help_text='Enter seasonality details')
    habitat = RichTextField(null=True, blank=True, help_text='Enter the species\' habitat')
    food = RichTextField(null=True, blank=True, help_text='Enter info larval and adult food sources')
    life_cycle = RichTextField(null=True, blank=True, help_text='Enter details about the life cycle')
    references = models.ManyToManyField('Reference', blank=True, related_name='species_pages',
        help_text='Enter citations used to write the info in the preciding fields')

    class Meta:
        ordering = ['species']
    
    def get_binomial(self):
        return f'{self.species.genus.name} {self.species.name}'
    
    def display_refs(self):
        return ', '.join([str(references.title) for references in self.references.all()])
    
    def __str__(self):
        return f'{self.species.genus.name} {self.species} page'

class Reference(models.Model):
    title = models.CharField(max_length=50)
    citation = RichTextField()

    def __str__(self):
        return f'{self.citation}'
