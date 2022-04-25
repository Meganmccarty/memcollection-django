from factory import SubFactory
from factory.django import DjangoModelFactory
from geography.factories import (
    CountryFactory,
    StateFactory,
    CountyFactory,
    LocalityUnderCountyFactory,
    GPSFactory,
    CollectingTripFactory
)
from taxonomy.factories import (
    OrderFactory,
    FamilyFactory,
    SubfamilyFactory,
    TribeFactory,
    GenusFactory,
    SpeciesFactory,
    SubspeciesFactory
)
from specimens.models import Person, SpecimenRecord, SpecimenRecordImage

class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person
    
    first_name = 'Megan'
    middle_initial = 'E'
    last_name = 'McCarty'

class SpecimenRecordFactory(DjangoModelFactory):
    class Meta:
        model = SpecimenRecord
    
    usi = 'MEM-100000'

    order = SubFactory(OrderFactory)
    family = SubFactory(FamilyFactory)
    subfamily = SubFactory(SubfamilyFactory)
    tribe = SubFactory(TribeFactory)
    genus = SubFactory(GenusFactory)
    species = SubFactory(SpeciesFactory)
    subspecies = SubFactory(SubspeciesFactory)