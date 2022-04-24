import datetime

from decimal import Decimal
from factory import SubFactory, SelfAttribute, LazyAttribute, post_generation
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

class CollectingTripFactory(DjangoModelFactory):
    class Meta:
        model = CollectingTrip
    
    name = 'Texas Trip'
    start_date = datetime.date(2001, 4, 17)
    end_date = datetime.date(2001, 4, 23)
    notes = 'We visited lots of places and caught lots of things!'

    @post_generation
    def states(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for state in extracted:
                self.states.add(state)