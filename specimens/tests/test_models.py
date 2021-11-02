from django.test import TestCase
from specimens.models import Person, SpecimenRecord, SpecimenRecordImage

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