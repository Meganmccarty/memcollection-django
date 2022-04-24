from decimal import Decimal
from factory import SubFactory, SelfAttribute, LazyAttribute
from factory.django import DjangoModelFactory
from django.contrib.contenttypes.models import ContentType
from geography.models import Country, State, County, Locality, GPS, CollectingTrip

class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country
    
    name = 'United States of America'
    abbr = 'USA'

class StateFactory(DjangoModelFactory):
    class Meta:
        model = State
    
    country = SubFactory(CountryFactory)
    name = 'Indiana'
    abbr = 'IN'

class CountyFactory(DjangoModelFactory):
    class Meta:
        model = County
    
    state = SubFactory(StateFactory)
    name = 'Switzerland'

class BaseLocalityFactory(DjangoModelFactory):
    class Meta:
        abstract = True
        exclude = ['content_object']

    object_id = SelfAttribute('content_object.id')
    content_type = LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )

class LocalityUnderCountyFactory(BaseLocalityFactory):
    class Meta:
        model = Locality
    
    content_object = SubFactory(CountyFactory)
    name = 'Boone Robinson Rd'
    range = '4 km NW'
    town = 'Patriot'

class LocalityUnderStateFactory(BaseLocalityFactory):
    class Meta:
        model = Locality
    
    content_object = SubFactory(StateFactory)
    name = 'Big Oaks National Wildlife Refuge'

class LocalityUnderCountryFactory(BaseLocalityFactory):
    class Meta:
        model = Locality
    
    content_object = SubFactory(CountryFactory)
    name = 'Carolina Biological Supply Company'

class GPSFactory(DjangoModelFactory):
    class Meta:
        model = GPS
    
    locality = SubFactory(LocalityUnderCountyFactory)
    latitude = Decimal('38.993340')
    longitude = Decimal('-109.1234560')
    elevation = 1500