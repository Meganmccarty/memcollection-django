from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from taxonomy.models import Species

class SpeciesPage(models.Model):
    species = models.OneToOneField(Species, on_delete=models.SET_NULL, null=True,
        related_name='species_page', help_text='Select the species for this page')
    title = models.SlugField(default='', null=True, blank=True, max_length=100)
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
    
    def genus(self):
        return {
            "name": f'{self.species.genus.name}',
            "common_name": f'{self.species.genus.common_name}',
            "authority": f'{self.species.genus.authority}'
        }
    
    def tribe(self):
        return {
            "name": f'{self.species.genus.tribe.name}',
            "common_name": f'{self.species.genus.tribe.common_name}',
            "authority": f'{self.species.genus.tribe.authority}'
        }
    
    def subfamily(self):
        return {
            "name": f'{self.species.genus.tribe.subfamily.name}',
            "common_name": f'{self.species.genus.tribe.subfamily.common_name}',
            "authority": f'{self.species.genus.tribe.subfamily.authority}'
        }
    
    def family(self):
        return {
            "name": f'{self.species.genus.tribe.subfamily.family.name}',
            "common_name": f'{self.species.genus.tribe.subfamily.family.common_name}',
            "authority": f'{self.species.genus.tribe.subfamily.family.authority}'
        }
    
    def order(self):
        return {
            "name": f'{self.species.genus.tribe.subfamily.family.order.name}',
            "common_name": f'{self.species.genus.tribe.subfamily.family.order.common_name}',
            "authority": f'{self.species.genus.tribe.subfamily.family.order.authority}'
        }
    
    def get_not_none_field(self, field):
        if field is None:
            return ''
        else:
            return field
    
    def get_taxonomy(self):
        return self.get_not_none_field(self.taxonomy)
    
    def get_description(self):
        return self.get_not_none_field(self.description)
    
    def get_distribution(self):
        return self.get_not_none_field(self.distribution)
    
    def get_seasonality(self):
        return self.get_not_none_field(self.seasonality)
    
    def get_habitat(self):
        return self.get_not_none_field(self.habitat)
    
    def get_food(self):
        return self.get_not_none_field(self.food)
    
    def get_life_cycle(self):
        return self.get_not_none_field(self.life_cycle)
    
    def display_refs(self):
        return ', '.join([str(references.title) for references in self.references.all()])
    
    def __str__(self):
        return f'{self.title} page'
    
    def save(self, *args, **kwargs):
        self.title = slugify(self.get_binomial())
        super(SpeciesPage, self).save(*args, **kwargs)

class Reference(models.Model):
    title = models.CharField(max_length=50)
    citation = RichTextField()

    def __str__(self):
        return f'{self.citation}'
