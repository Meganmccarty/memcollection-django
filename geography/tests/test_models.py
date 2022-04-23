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
    
    def test_render_county_abbr(self):
        county = factories.CountyFactory()
        alaska = factories.StateFactory(name='Alaska')
        louisiana = factories.StateFactory(name='Louisiana')
        borough = factories.CountyFactory(name='Fairbanks N. Star', state=alaska)
        area = factories.CountyFactory(name='Yukon-Koyukuk Census Area', state=alaska)
        parish = factories.CountyFactory(name='Allen', state=louisiana)

        self.assertEqual(county.render_county_abbr(), 'Switzerland Co.')
        self.assertEqual(borough.render_county_abbr(), 'Fairbanks N. Star Boro.')
        self.assertEqual(area.render_county_abbr(), 'Yukon-Koyukuk Census Area')
        self.assertEqual(parish.render_county_abbr(), 'Allen Par.')