from django.test import TestCase
from geography import factories
from geography.models import Country, State, County, Locality, GPS, CollectingTrip

class TestCountryModel(TestCase):
    "Tests for Country Model"

    def test_country_str_equals_name(self):
        country_usa = factories.CountryFactory()
        self.assertEqual(country_usa.__str__(), 'United States of America')