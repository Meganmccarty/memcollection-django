from django.db.models.query_utils import subclasses
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from geography.models import CollectingTrip, Country, State, County, Locality, GPS
from specimens.models import Person, SpecimenRecord, SpecimenRecordImage
from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="Joe", middle_initial="M", last_name="Smith", suffix="Jr.")
        Person.objects.create(first_name="Jane", middle_initial="A", last_name="Doe")
        Person.objects.create(first_name="Tim", last_name="Johnson")
    
    def test_get_middle_initial(self):
        joe = Person.objects.get(first_name="Joe")
        jane = Person.objects.get(first_name="Jane")
        tim = Person.objects.get(first_name="Tim")

        self.assertEqual(joe.get_middle_initial(), " M.")
        self.assertEqual(jane.get_middle_initial(), " A.")
        self.assertEqual(tim.get_middle_initial(), "")

    def test_get_suffix(self):
        joe = Person.objects.get(first_name="Joe")
        jane = Person.objects.get(first_name="Jane")
        tim = Person.objects.get(first_name="Tim")

        self.assertEqual(joe.get_suffix(), ", Jr.")
        self.assertEqual(jane.get_suffix(), "")
        self.assertEqual(tim.get_suffix(), "")
    
    def test_colletor_name(self):
        joe = Person.objects.get(first_name="Joe")
        jane = Person.objects.get(first_name="Jane")
        tim = Person.objects.get(first_name="Tim")

        self.assertEqual(joe.collector_name(), "J. Smith, Jr.")
        self.assertEqual(jane.collector_name(), "J. Doe")
        self.assertEqual(tim.collector_name(), "T. Johnson")

    def test_string(self):
        joe = Person.objects.get(first_name="Joe")
        jane = Person.objects.get(first_name="Jane")
        tim = Person.objects.get(first_name="Tim")

        self.assertEqual(joe.__str__(), "Joe M. Smith, Jr.")
        self.assertEqual(jane.__str__(), "Jane A. Doe")
        self.assertEqual(tim.__str__(), "Tim Johnson")

class SpecimenRecordTestCase(TestCase):
    def setUp(self):
        joe = Person.objects.create(first_name="Joe", middle_initial="M", last_name="Smith", suffix="Jr.")
        jane = Person.objects.create(first_name="Jane", middle_initial="A", last_name="Doe")
        tim = Person.objects.create(first_name="Tim", last_name="Johnson")

        lepidoptera = Order.objects.create(name="Lepidoptera", common_name="Butterflies and Moths", 
            authority="Linnaeus, 1758")
        papilionidae = Family.objects.create(order=lepidoptera, name="Papilionidae", common_name="Swallowtails and Parnassians",
            authority="Latreille, [1802]")
        papilioninae = Subfamily.objects.create(family=papilionidae, name="Papilioninae", common_name="Swallowtails",
            authority="Latreille, [1802]")
        papilionini = Tribe.objects.create(subfamily=papilioninae, name="Papilionini", common_name="", authority="Latreille, [1802]")
        papilio = Genus.objects.create(tribe=papilionini, name="Papilio", common_name="", authority="Linnaeus, 1758")
        machaon = Species.objects.create(genus=papilio, name="machaon", common_name="Old World Swallowtail",
            authority="Linnaeus, 1758", mona=4166.0, p3=770298.0)
        bairdii = Subspecies.objects.create(species=machaon, name="bairdii", common_name="Baird's Swallowtail",
            authority="Edwards, 1866", mona=4164.0, p3=770298.0)

        usa = Country.objects.create(name="United States of America", abbr="USA")
        indiana = State.objects.create(country=usa, name="Indiana", abbr="IN")
        kentucky = State.objects.create(country=usa, name="Kentucky", abbr="KY")
        switzerland = County.objects.create(state=indiana, name="Switzerland")
        boone_robinson = Locality.objects.create(object_id=switzerland.id,
            content_type=ContentType.objects.get(app_label="geography", model="county"),
            name="Boone Robinson Rd", range="4 km NW", town="Patriot")
        boone_robinson_gps = GPS.objects.create(locality=boone_robinson, latitude=35.54, longitude=85.58, 
            elevation="254")
        indiana_trip = CollectingTrip.objects.create(name="Indiana 2015", start_date="2015-07-15", end_date="2015-07-25")
        indiana_trip.states.set([indiana, kentucky])

        specimen1 = SpecimenRecord.objects.create(
            usi="MEM-Test-01", order=lepidoptera, family=papilionidae, subfamily=papilioninae, tribe=papilionini,
            genus=papilio, species=machaon, subspecies=bairdii, determiner=joe, determined_year=2015, sex="male",
            stage="adult", preparer=joe, preparation="spread", preparation_date="2015-07-25", labels_printed=True,
            labeled=False, photographed=False, identified=True, collecting_trip=indiana_trip, country=usa,
            state=indiana, county=switzerland, locality=boone_robinson, gps=boone_robinson_gps,
            day=20, month="July", year=2015, method="net", weather="sunny",
            temperature=85, time_of_day="12:05 PM", habitat="Found in field", notes="Did not relax specimen"
        )
        specimen1.collector.set([joe, jane, tim])
        specimen2 = SpecimenRecord.objects.create(
            usi="MEM-Test-02", order=lepidoptera, family=papilionidae, subfamily=papilioninae, tribe=papilionini,
            genus=papilio, determiner=jane, determined_year=2017, sex="female", stage="adult", preparer=jane,
            preparation="spread", preparation_date="2017-06-05", labels_printed=False, labeled=False,
            photographed=True, identified=False, country=usa, state=indiana, month="June", year=2017,
            method="net", weather="cloudy", temperature=80
        )
        specimen2.collector.set([jane])
        specimen3 = SpecimenRecord.objects.create(
            usi="MEM-Test-03", order=lepidoptera, determiner=tim, determined_year=2020, sex="female",
            stage="adult", preparer=tim, preparation="spread", labels_printed=True,
            labeled=True, photographed=True, identified=False, country=usa,
            state=indiana, county=switzerland, locality=boone_robinson, year=2020, method="net"
        )
        specimen3.collector.set([joe, tim])
        specimen4 = SpecimenRecord.objects.create(
            usi="MEM-Test-04", order=lepidoptera, sex="male", stage="adult", labels_printed=True,
            labeled=True, photographed=True, identified=False, country=usa,
            state=indiana, county=switzerland, locality=boone_robinson, day=24, month="November", year=2018, method="net"
        )
        specimen4.collector.set([joe])
    
    def test_taxon(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")

        self.assertEqual(specimen1.taxon(), {
            "name": "Papilio machaon bairdii",
            "authority": "Edwards, 1866",
            "common_name": "Baird's Swallowtail",
            "mona": 4164.00,
            "p3": 770298.00
        })
        self.assertEqual(specimen2.taxon(), {
            "name": "Papilio",
            "authority": "Linnaeus, 1758",
            "common_name": ""
        })
        self.assertEqual(specimen3.taxon(), {
            "name": "Lepidoptera",
            "authority": "Linnaeus, 1758",
            "common_name": "Butterflies and Moths"
        })
    
    def test_collected_date(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")

        self.assertEqual(specimen1.collected_date(), "20-Jul-2015")
        self.assertEqual(specimen2.collected_date(), "June 2017")
        self.assertEqual(specimen3.collected_date(), "2020")
    
    def test_full_date(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")

        self.assertEqual(specimen1.full_date(), "20 July 2015")
        self.assertEqual(specimen2.full_date(), "June 2017")
        self.assertEqual(specimen3.full_date(), "2020")
    
    def test_num_date(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")
        specimen4 = SpecimenRecord.objects.get(usi="MEM-Test-04")

        self.assertEqual(specimen1.num_date(), "2015-07-20")
        self.assertEqual(specimen2.num_date(), "2017-06")
        self.assertEqual(specimen3.num_date(), "2020")
        self.assertEqual(specimen4.num_date(), "2018-11-24")
    
    def test_display_collectors(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")

        self.assertEqual(specimen1.display_collectors(), "J. Doe, T. Johnson, J. Smith, Jr.")
        self.assertEqual(specimen2.display_collectors(), "J. Doe")
        self.assertEqual(specimen3.display_collectors(), "T. Johnson, J. Smith, Jr.")

    def test_display_preparer(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen4 = SpecimenRecord.objects.get(usi="MEM-Test-04")

        self.assertEqual(specimen1.display_preparer(), "Joe Smith, Jr.")
        self.assertEqual(specimen4.display_preparer(), "")
    
    def test_display_determiner(self):
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")
        specimen4 = SpecimenRecord.objects.get(usi="MEM-Test-04")

        self.assertEqual(specimen3.display_determiner(), "Tim Johnson")
        self.assertEqual(specimen4.display_determiner(), "")
    
    def test_temp_F(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")
        DEGREE_SIGN = u'\N{DEGREE SIGN}'

        self.assertEqual(specimen1.temp_F(), f'85.0{DEGREE_SIGN}F')
        self.assertEqual(specimen2.temp_F(), f'80.0{DEGREE_SIGN}F')
        self.assertEqual(specimen3.temp_F(), "")
    
    def test_temp_C(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")
        specimen3 = SpecimenRecord.objects.get(usi="MEM-Test-03")
        DEGREE_SIGN = u'\N{DEGREE SIGN}'

        self.assertEqual(specimen1.temp_C(), f'29.4{DEGREE_SIGN}C')
        self.assertEqual(specimen2.temp_C(), f'26.7{DEGREE_SIGN}C')
        self.assertEqual(specimen3.temp_C(), "")

    def test__str__(self):
        specimen1 = SpecimenRecord.objects.get(usi="MEM-Test-01")
        specimen2 = SpecimenRecord.objects.get(usi="MEM-Test-02")

        self.assertEqual(specimen1.__str__(), "MEM-Test-01")
        self.assertEqual(specimen2.__str__(), "MEM-Test-02")