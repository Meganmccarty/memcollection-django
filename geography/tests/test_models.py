from decimal import Decimal
from django.test import TestCase
from geography import factories
from geography.models import Country, State, County, Locality, GPS, CollectingTrip

class TestCountryModel(TestCase):
    """Tests for Country Model"""

    def test_country_str_equals_name(self):
        country_usa = factories.CountryFactory()
        self.assertEqual(country_usa.__str__(), 'United States of America')

class TestStateModel(TestCase):
    """Tests for State Model"""

    def test_state_str_equals_name(self):
        state_indiana = factories.StateFactory()
        self.assertEqual(state_indiana.__str__(), 'Indiana')
    
    def test_state_belongs_to_country(self):
        state_indiana = factories.StateFactory()
        self.assertEqual(state_indiana.country.name, 'United States of America')

class TestCountyModel(TestCase):
    """Tests for County Model"""

    def test_county_str_equals_name(self):
        county_switzerland = factories.CountyFactory()
        self.assertEqual(county_switzerland.__str__(), 'Switzerland')
    
    def test_county_belongs_to_state(self):
        county_switzerland = factories.CountyFactory()
        self.assertEqual(county_switzerland.state.name, 'Indiana')
    
    def test_render_county_abbr_for_county(self):
        county = factories.CountyFactory()
        self.assertEqual(county.render_county_abbr(), 'Switzerland Co.')
    
    def test_render_county_abbr_for_borough(self):
        alaska = factories.StateFactory(name='Alaska')
        borough = factories.CountyFactory(name='Fairbanks N. Star', state=alaska)
        self.assertEqual(borough.render_county_abbr(), 'Fairbanks N. Star Boro.')
    
    def test_render_county_abbr_for_area(self):
        alaska = factories.StateFactory(name='Alaska')
        area = factories.CountyFactory(name='Yukon-Koyukuk Census Area', state=alaska)
        self.assertEqual(area.render_county_abbr(), 'Yukon-Koyukuk Census Area')
    
    def test_render_county_abbr_for_parish(self):
        louisiana = factories.StateFactory(name='Louisiana')
        parish = factories.CountyFactory(name='Allen', state=louisiana)
        self.assertEqual(parish.render_county_abbr(), 'Allen Par.')

class TestLocalityModel(TestCase):
    """Tests for Locality Model"""

    def test_locality_under_country_with_name_only(self):
        locality = factories.LocalityUnderCountryFactory(name='Carolina Biological Supply Company', range='', town='')
        self.assertEqual(locality.__str__(), 'Carolina Biological Supply Company')
    
    def test_locality_under_country_with_town_only(self):
        locality = factories.LocalityUnderCountryFactory(name='', range='', town='Mexico City')
        self.assertEqual(locality.__str__(), '--,  Mexico City')
    
    def test_locality_under_country_with_range_and_town(self):
        locality = factories.LocalityUnderCountryFactory(name='', range='2 km NW', town='Gainesville')
        self.assertEqual(locality.__str__(), '--, 2 km NW Gainesville')
    
    def test_locality_under_state_with_name_only(self):
        locality = factories.LocalityUnderStateFactory(name='Rosemount Park', range='', town='')
        self.assertEqual(locality.__str__(), 'Rosemount Park')
    
    def test_locality_under_state_with_town_only(self):
        locality = factories.LocalityUnderStateFactory(name='', range='', town='Continential')
        self.assertEqual(locality.__str__(), '--,  Continential')
    
    def test_locality_under_state_with_range_and_town(self):
        locality = factories.LocalityUnderStateFactory(name='', range='10 km N', town='Continential')
        self.assertEqual(locality.__str__(), '--, 10 km N Continential')
    
    def test_locality_under_county_with_name_only(self):
        locality = factories.LocalityUnderCountyFactory(name='Noxubee National Wildlife Refuge', range='', town='')
        self.assertEqual(locality.__str__(), 'Noxubee National Wildlife Refuge')
    
    def test_locality_under_county_with_town_only(self):
        locality = factories.LocalityUnderCountyFactory(name='', range='', town='Continentially')
        self.assertEqual(locality.__str__(), '--,  Continentially')
    
    def test_locality_under_county_with_range_and_town(self):
        locality = factories.LocalityUnderCountyFactory(name='', range='10 km W', town='Patriot')
        self.assertEqual(locality.__str__(), '--, 10 km W Patriot')

class TestGPSModel(TestCase):
    """Tests for GPS Model"""

    def test_normalize_latitude(self):
        gps = factories.GPSFactory()
        self.assertEqual(gps.normalize_latitude(), Decimal('38.99334'))
    
    def test_normalize_longitude(self):
        gps = factories.GPSFactory()
        self.assertEqual(gps.normalize_longitude(), Decimal('-109.123456'))
    
    def test_add_m_to_elevation(self):
        gps = factories.GPSFactory()
        self.assertEqual(gps.elevation_and_meters(), '1500m')
    
    def test_gps_str_equals_norm_coors(self):
        gps = factories.GPSFactory()
        self.assertEqual(gps.__str__(), '38.99334 -109.123456')

class TestCollectingTripModel(TestCase):
    """Tests for CollectingTrip Model"""

    def test_collectingtrip_str_equals_name(self):
        trip = factories.CollectingTripFactory()
        self.assertEqual(trip.__str__(), 'Texas Trip')
    
    def test_collectingtrip_states_str(self):
        texas = factories.StateFactory(name='Texas')
        louisiana = factories.StateFactory(name='Louisiana')
        oklahoma = factories.StateFactory(name='Oklahoma')
        trip = factories.CollectingTripFactory(states=(texas, louisiana, oklahoma))
        self.assertEqual(trip.states_collected(), 'Louisiana, Oklahoma, Texas')