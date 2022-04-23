from factory import SubFactory
from factory.django import DjangoModelFactory
from geography.models import Country, State, County, Locality, GPS, CollectingTrip

class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country
    
    name = 'United States of America'
    abbr = 'USA'