import datetime

from factory import SubFactory, post_generation
from factory.django import DjangoModelFactory
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

    preparer = SubFactory(PersonFactory)
    determiner = SubFactory(PersonFactory)

    @post_generation
    def collector(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for person in extracted:
                self.collector.add(person)

class SpecimenRecordImageFactory(DjangoModelFactory):
    class Meta:
        model = SpecimenRecordImage
    
    usi = SubFactory(SpecimenRecordFactory)
    date = datetime.date(2001, 6, 15)