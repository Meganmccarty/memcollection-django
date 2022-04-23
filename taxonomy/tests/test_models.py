from django.test import TestCase
from taxonomy import factories
from taxonomy.models import TaxonomyBaseInfo, Order, Family, Subfamily, Tribe, Genus, Species, Subspecies

class TestOrderModel(TestCase):
    "Tests for Order Model"

    def test_order_subclasses_from_taxonomybase(self):
        self.assertTrue(issubclass(Order, TaxonomyBaseInfo))

    def test_order_str_equals_name(self):
        order_lepidoptera = factories.OrderFactory()
        self.assertEqual(order_lepidoptera.__str__(), 'Lepidoptera')

class TestTaxonomyModels(TestCase):
    def setUp(self):
        order = Order.objects.create(
            name='Test Order Name',
            common_name='Test Order Common Name',
            authority='Test Order Authority'
        )
        family = Family.objects.create(
            order=order,
            name='Test Family Name',
            common_name='Test Family Common Name',
            authority='Test Family Authority'
        )
        subfamily = Subfamily.objects.create(
            family=family,
            name='Test Subfamily Name',
            common_name='Test Subfamily Common Name',
            authority='Test Subfamily Authority'
        )
        tribe = Tribe.objects.create(
            subfamily=subfamily,
            name='Test Tribe Name',
            common_name='Test Tribe Common Name',
            authority='Test Tribe Authority'
        )
        genus = Genus.objects.create(
            tribe=tribe,
            name='Test Genus Name',
            common_name='Test Genus Common Name',
            authority='Test Genus Authority'
        )
        species = Species.objects.create(
            genus=genus,
            name='Test Species Name',
            common_name='Test Species Common Name',
            authority='Test Species Authority'
        )
        Subspecies.objects.create(
            species=species,
            name='Test Subspecies Name',
            common_name='Test Subspecies Common Name',
            authority='Test Subspecies Authority'
        )
    def test_subclasses_order_model_base(self):
        self.assertTrue(issubclass(Order, TaxonomyBaseInfo))
    
    def test_subclasses_family_model_base(self):
        self.assertTrue(issubclass(Family, TaxonomyBaseInfo))
    
    def test_subclasses_subfamily_model_base(self):
        self.assertTrue(issubclass(Subfamily, TaxonomyBaseInfo))
    
    def test_subclasses_tribe_model_base(self):
        self.assertTrue(issubclass(Tribe, TaxonomyBaseInfo))
    
    def test_subclasses_genus_model_base(self):
        self.assertTrue(issubclass(Genus, TaxonomyBaseInfo))
    
    def test_subclasses_species_model_base(self):
        self.assertTrue(issubclass(Species, TaxonomyBaseInfo))
    
    def test_subclasses_subspecies_model_base(self):
        self.assertTrue(issubclass(Subspecies, TaxonomyBaseInfo))
    
    def test_order_model_str(self):
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), 'Test Order Name')
    
    def test_family_model_str(self):
        family = Family.objects.get(id=1)
        self.assertEqual(str(family), 'Test Family Name')
    
    def test_subfamily_model_str(self):
        subfamily = Subfamily.objects.get(id=1)
        self.assertEqual(str(subfamily), 'Test Subfamily Name')
    
    def test_tribe_model_str(self):
        tribe = Tribe.objects.get(id=1)
        self.assertEqual(str(tribe), 'Test Tribe Name')
    
    def test_genus_model_str(self):
        genus = Genus.objects.get(id=1)
        self.assertEqual(str(genus), 'Test Genus Name')
    
    def test_species_model_str(self):
        species = Species.objects.get(id=1)
        self.assertEqual(str(species), 'Test Species Name')
    
    def test_subspecies_model_str(self):
        subspecies = Subspecies.objects.get(id=1)
        self.assertEqual(str(subspecies), 'Test Subspecies Name')