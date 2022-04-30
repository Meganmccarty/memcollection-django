from contextlib import nullcontext
from django.db.models.query_utils import subclasses
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from geography.models import CollectingTrip, Country, State, County, Locality, GPS
from specimens.models import Person, SpecimenRecord, SpecimenRecordImage
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies

from specimens.factories import PersonFactory, SpecimenRecordFactory

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
    
    # def setUp(self):
    #     joe = Person.objects.create(first_name="Joe", middle_initial="M", last_name="Smith", suffix="Jr.")
    #     jane = Person.objects.create(first_name="Jane", middle_initial="A", last_name="Doe")
    #     tim = Person.objects.create(first_name="Tim", last_name="Johnson")

    #     lepidoptera = Order.objects.create(name="Lepidoptera", common_name="Butterflies and Moths", 
    #         authority="Linnaeus, 1758")
    #     papilionidae = Family.objects.create(order=lepidoptera, name="Papilionidae", common_name="Swallowtails and Parnassians",
    #         authority="Latreille, [1802]")
    #     papilioninae = Subfamily.objects.create(family=papilionidae, name="Papilioninae", common_name="Swallowtails",
    #         authority="Latreille, [1802]")
    #     papilionini = Tribe.objects.create(subfamily=papilioninae, name="Papilionini", common_name="", authority="Latreille, [1802]")
    #     papilio = Genus.objects.create(tribe=papilionini, name="Papilio", common_name="", authority="Linnaeus, 1758")
    #     machaon = Species.objects.create(genus=papilio, name="machaon", common_name="Old World Swallowtail",
    #         authority="Linnaeus, 1758", mona=4166.0, p3=770298.0)
    #     bairdii = Subspecies.objects.create(species=machaon, name="bairdii", common_name="Baird's Swallowtail",
    #         authority="Edwards, 1866", mona=4164.0, p3=770298.0)

    #     usa = Country.objects.create(name="United States of America", abbr="USA")
    #     indiana = State.objects.create(country=usa, name="Indiana", abbr="IN")
    #     kentucky = State.objects.create(country=usa, name="Kentucky", abbr="KY")
    #     switzerland = County.objects.create(state=indiana, name="Switzerland")
    #     boone_robinson = Locality.objects.create(object_id=switzerland.id,
    #         content_type=ContentType.objects.get(app_label="geography", model="county"),
    #         name="Boone Robinson Rd", range="4 km NW", town="Patriot")
    #     boone_robinson_gps = GPS.objects.create(locality=boone_robinson, latitude=35.54, longitude=85.58, 
    #         elevation="254")
    #     indiana_trip = CollectingTrip.objects.create(name="Indiana 2015", start_date="2015-07-15", end_date="2015-07-25")
    #     indiana_trip.states.set([indiana, kentucky])

    #     specimen1 = SpecimenRecord.objects.create(
    #         usi="MEM-Test-01", order=lepidoptera, family=papilionidae, subfamily=papilioninae, tribe=papilionini,
    #         genus=papilio, species=machaon, subspecies=bairdii, determiner=joe, determined_year=2015, sex="male",
    #         stage="adult", preparer=joe, preparation="spread", preparation_date="2015-07-25", labels_printed=True,
    #         labeled=False, photographed=False, identified=True, collecting_trip=indiana_trip, country=usa,
    #         state=indiana, county=switzerland, locality=boone_robinson, gps=boone_robinson_gps,
    #         day=2, month="July", year=2015, method="net", weather="sunny",
    #         temperature=85, time_of_day="12:05 PM", habitat="Found in field", notes="Did not relax specimen"
    #     )
    #     specimen1.collector.set([joe, jane, tim])
    #     specimen2 = SpecimenRecord.objects.create(
    #         usi="MEM-Test-02", order=lepidoptera, family=papilionidae, subfamily=papilioninae, tribe=papilionini,
    #         genus=papilio, determiner=jane, determined_year=2017, sex="female", stage="adult", preparer=jane,
    #         preparation="spread", preparation_date="2017-06-05", labels_printed=False, labeled=False,
    #         photographed=True, identified=False, country=usa, state=indiana, month="June", year=2017,
    #         method="net", weather="cloudy", temperature=80
    #     )
    #     specimen2.collector.set([jane])
    #     specimen3 = SpecimenRecord.objects.create(
    #         usi="MEM-Test-03", order=lepidoptera, determiner=tim, determined_year=2020, sex="female",
    #         stage="adult", preparer=tim, preparation="spread", labels_printed=True,
    #         labeled=True, photographed=True, identified=False, country=usa,
    #         state=indiana, county=switzerland, locality=boone_robinson, year=2020, method="net"
    #     )
    #     specimen3.collector.set([joe, tim])
    #     specimen4 = SpecimenRecord.objects.create(
    #         usi="MEM-Test-04", order=lepidoptera, sex="male", stage="adult", labels_printed=True,
    #         labeled=True, photographed=True, identified=False, country=usa,
    #         state=indiana, county=switzerland, locality=boone_robinson, day=24, month="November", year=2018, method="net"
    #     )
    #     specimen4.collector.set([joe])
    
    # def test_temp_F(self):
    #     specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
    #     specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
    #     specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")
    #     DEGREE_SIGN = u'\N{DEGREE SIGN}'

    #     self.assertEqual(specimen1.temp_F(), f'85.0{DEGREE_SIGN}F')
    #     self.assertEqual(specimen2.temp_F(), f'80.0{DEGREE_SIGN}F')
    #     self.assertEqual(specimen3.temp_F(), "")
    
    # def test_temp_C(self):
    #     specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
    #     specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
    #     specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")
    #     DEGREE_SIGN = u'\N{DEGREE SIGN}'

    #     self.assertEqual(specimen1.temp_C(), f'29.4{DEGREE_SIGN}C')
    #     self.assertEqual(specimen2.temp_C(), f'26.7{DEGREE_SIGN}C')
    #     self.assertEqual(specimen3.temp_C(), "")

    # def test__str__(self):
    #     specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
    #     specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")

    #     self.assertEqual(specimen1.__str__(), "MEM-Test-01")
    #     self.assertEqual(specimen2.__str__(), "MEM-Test-02")