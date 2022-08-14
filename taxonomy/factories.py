from factory import SubFactory
from factory.django import DjangoModelFactory
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
    
    name = 'Lepidoptera'
    common_name = 'Butterflies and Moths'
    authority = 'Linnaeus, 1758'

class FamilyFactory(DjangoModelFactory):
    class Meta:
        model = Family
    
    order = SubFactory(OrderFactory)
    name = 'Papilionidae'
    common_name = 'Swallowtails and Parnassians'
    authority = 'Linnaeus, 1758'

class SubfamilyFactory(DjangoModelFactory):
    class Meta:
        model = Subfamily
    
    family = SubFactory(FamilyFactory)
    name = 'Papilioninae'
    common_name = 'Swallowtails'
    authority = 'Linnaeus, 1758'

class TribeFactory(DjangoModelFactory):
    class Meta:
        model = Tribe
    
    subfamily = SubFactory(SubfamilyFactory)
    name = 'Papilionini'
    common_name = ''
    authority = 'Linnaeus, 1758'

class GenusFactory(DjangoModelFactory):
    class Meta:
        model = Genus
    
    tribe = SubFactory(TribeFactory)
    name = 'Papilio'
    common_name = ''
    authority = 'Linnaeus, 1758'

class SpeciesFactory(DjangoModelFactory):
    class Meta:
        model = Species
    
    genus = SubFactory(GenusFactory)
    name = 'machaon'
    common_name = 'Old World Swallowtail'
    authority = 'Linnaeus, 1758'
    mona = 4166.00
    p3 = 770298.00

class SubspeciesFactory(DjangoModelFactory):
    class Meta:
        model = Subspecies
    
    species = SubFactory(SpeciesFactory)
    name = 'bairdii'
    common_name = 'Baird\'s Swallowtail'
    authority = 'Edwards, 1866'
    mona = 4164.00
    p3 = 770298.00