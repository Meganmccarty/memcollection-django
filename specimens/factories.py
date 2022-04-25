from factory import SubFactory
from factory.django import DjangoModelFactory
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies
from specimens.models import Person, SpecimenRecord, SpecimenRecordImage

class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person
    
    first_name = 'Megan'
    middle_initial = 'E'
    last_name = 'McCarty'