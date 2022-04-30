from contextlib import nullcontext
from django.db.models.query_utils import subclasses
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from geography.models import CollectingTrip, Country, State, County, Locality, GPS
from specimens.models import Person, SpecimenRecord, SpecimenRecordImage
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies

from specimens.factories import PersonFactory, SpecimenRecordFactory, SpecimenRecordImageFactory

class PersonTestCase(TestCase):
    """Tests for Person Model"""

    def test_get_middle_initial(self):
        megan = PersonFactory()
        doe = PersonFactory(first_name='John', middle_initial='', last_name='Doe')
        self.assertEqual(megan.get_middle_initial(), ' E.')
        self.assertEqual(doe.get_middle_initial(), '')
    
    def test_get_suffix(self):
        megan = PersonFactory()
        doe = PersonFactory(first_name='John', middle_initial='', last_name='Doe', suffix='Jr.')
        self.assertEqual(megan.get_suffix(), '')
        self.assertEqual(doe.get_suffix(), ' Jr.')
    
    def test_get_name(self):
        megan = PersonFactory()
        doe = PersonFactory(first_name='John', middle_initial='', last_name='Doe', suffix='Jr.')
        self.assertEqual(megan.get_name(), 'Megan McCarty')
        self.assertEqual(doe.get_name(), 'John Doe Jr.')
    
    def test_collector_name(self):
        megan = PersonFactory()
        doe = PersonFactory(first_name='John', middle_initial='', last_name='Doe', suffix='Jr.')
        self.assertEqual(megan.collector_name(), 'M. McCarty')
        self.assertEqual(doe.collector_name(), 'J. Doe Jr.')
    
    def test_person_str_equals_full_name(self):
        megan = PersonFactory()
        doe = PersonFactory(first_name='John', middle_initial='', last_name='Doe', suffix='Jr.')
        self.assertEqual(megan.__str__(), 'Megan E. McCarty')
        self.assertEqual(doe.__str__(), 'John Doe Jr.')

class SpecimenRecordTestCase(TestCase):
    """Tests for SpecimenRecord Model"""
    
    def test_convert_to_json(self):
        specimen_species = SpecimenRecordFactory(subspecies=None)
        specimen_genus = SpecimenRecordFactory(species=None, subspecies=None)

        self.assertEqual(
            specimen_species.convert_to_json(),
            {
                'id': specimen_species.species.id,
                'name': 'machaon',
                'authority': 'Linnaeus, 1758',
                'common_name': 'Old World Swallowtail',
                'mona': 4166.00,
                'p3': 770298.00 
            }
        )
        self.assertEqual(
            specimen_genus.convert_to_json(),
            {
                'id': specimen_genus.genus.id,
                'name': 'Papilio',
                'authority': 'Linnaeus, 1758',
                'common_name': ''
            }
        )

    def test_generating_lowest_taxon_level(self):
        specimen_subspecies = SpecimenRecordFactory()
        specimen_species = SpecimenRecordFactory(subspecies=None)
        specimen_genus = SpecimenRecordFactory(species=None, subspecies=None)

        self.assertEqual(
            specimen_subspecies.taxon(),
            {
                'id': specimen_subspecies.subspecies.id,
                'name': 'Papilio machaon bairdii',
                'common_name': 'Baird\'s Swallowtail',
                'authority': 'Edwards, 1866',
                'mona': 4164.00,
                'p3': 770298.00
            }
        )
        self.assertEqual(
            specimen_species.taxon(),
            {
                'id': specimen_species.species.id,
                'name': 'Papilio machaon',
                'common_name': 'Old World Swallowtail',
                'authority': 'Linnaeus, 1758',
                'mona': 4166.00,
                'p3': 770298.00
            }
        )
        self.assertEqual(
            specimen_genus.taxon(),
            {
                'id': specimen_genus.genus.id,
                'name': 'Papilio',
                'common_name': '',
                'authority': 'Linnaeus, 1758'
            }
        )
    
    def test_get_collected_date(self):
        specimen_year = SpecimenRecordFactory(year=2004)
        specimen_year_month = SpecimenRecordFactory(year=2000, month='January')
        specimen_year_month_day = SpecimenRecordFactory(year=2001, month='February', day=15)

        self.assertEqual(specimen_year.get_collected_date(), '2004')
        self.assertEqual(specimen_year_month.get_collected_date(), 'January 2000')
        self.assertEqual(specimen_year_month_day.get_collected_date(), '15-Feb-2001')
    
    def test_get_full_date(self):
        specimen_year = SpecimenRecordFactory(year=2004)
        specimen_year_month = SpecimenRecordFactory(year=2000, month='January')
        specimen_year_month_day = SpecimenRecordFactory(year=2001, month='February', day=15)

        self.assertEqual(specimen_year.get_full_date(), '2004')
        self.assertEqual(specimen_year_month.get_full_date(), 'January 2000')
        self.assertEqual(specimen_year_month_day.get_full_date(), '15 February 2001')
    
    def test_get_num_date(self):
        specimen_year = SpecimenRecordFactory(year=2004)
        specimen_year_month = SpecimenRecordFactory(year=2000, month='January')
        specimen_year_month_day_15 = SpecimenRecordFactory(year=2001, month='February', day=15)
        specimen_year_month_day_1 = SpecimenRecordFactory(year=2001, month='October', day=1)

        self.assertEqual(specimen_year.get_num_date(), '2004')
        self.assertEqual(specimen_year_month.get_num_date(), '2000-01')
        self.assertEqual(specimen_year_month_day_15.get_num_date(), '2001-02-15')
        self.assertEqual(specimen_year_month_day_1.get_num_date(), '2001-10-01')
    
    def test_display_preparer(self):
        specimen_preparer = SpecimenRecordFactory()
        self.assertEqual(specimen_preparer.display_preparer(), 'Megan McCarty')

    def test_display_determiner(self):
        specimen_determiner= SpecimenRecordFactory()
        self.assertEqual(specimen_determiner.display_determiner(), 'Megan McCarty')
    
    def test_display_collectors(self):
        megan = PersonFactory()
        doe = PersonFactory(first_name='John', middle_initial='', last_name='Doe', suffix='Jr.')
        smith = PersonFactory(first_name='Tim', middle_initial='', last_name='Smith')
        specimen1 = SpecimenRecordFactory(collector=(megan, ))
        specimen2 = SpecimenRecordFactory(collector=(megan, smith))
        specimen3 = SpecimenRecordFactory(collector=(megan, smith, doe))

        self.assertEqual(specimen1.display_collectors(), 'M. McCarty')
        self.assertEqual(specimen2.display_collectors(), 'M. McCarty, T. Smith')
        self.assertEqual(specimen3.display_collectors(), 'J. Doe Jr., M. McCarty, T. Smith')
    
    def test_get_temp_F(self):
        specimen = SpecimenRecordFactory(temperature=75)
        self.assertEqual(specimen.get_temp_F(), '75°F')
    
    def test_get_temp_C(self):
        specimen = SpecimenRecordFactory(temperature=78)
        self.assertEqual(specimen.get_temp_C(), '25.6°C')
    
    def test_str_equals_usi(self):
        specimen = SpecimenRecordFactory()
        self.assertEqual(specimen.__str__(), 'MEM-100000')

class SpecimenRecordImageTestCase(TestCase):
    """Tests for SpecimenRecordImage Model"""

    def test_specimen_record_image_url(self):
        specimen_image = SpecimenRecordImageFactory(
            image = 'butterfly.jpg',
        )
        self.assertIn(f'{specimen_image.image}', specimen_image.get_image_url())
    
    def test_specimen_record_image_str_equals_usi(self):
        specimen = SpecimenRecordImageFactory()
        self.assertEqual(specimen.__str__(), 'MEM-100000')