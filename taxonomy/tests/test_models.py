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

class TestFamilyModel(TestCase):
    "Tests for Family Model"

    def test_family_subclasses_from_taxonomybase(self):
        self.assertTrue(issubclass(Family, TaxonomyBaseInfo))

    def test_family_str_equals_name(self):
        family_papilionidae = factories.FamilyFactory()
        self.assertEqual(family_papilionidae.__str__(), 'Papilionidae')
    
    def test_family_belongs_to_order(self):
        family_papilionidae = factories.FamilyFactory()
        self.assertEqual(family_papilionidae.order.name, 'Lepidoptera')
    
    def test_family_image_url_with_no_image(self):
        family_papilionidae = factories.FamilyFactory()
        self.assertEqual(family_papilionidae.get_image_url(), '')
    
    def test_family_image_url_with_image(self):
        family_papilionidae = factories.FamilyFactory(
            image = 'butterfly.jpg',
        )
        self.assertIn(f'{family_papilionidae.image}', family_papilionidae.get_image_url())

class TestSubfamilyModel(TestCase):
    "Tests for Subfamily Model"

    def test_subfamily_subclasses_from_taxonomybase(self):
        self.assertTrue(issubclass(Subfamily, TaxonomyBaseInfo))
    
    def test_subfamily_str_equals_name(self):
        subfamily_papilioninae = factories.SubfamilyFactory()
        self.assertEqual(subfamily_papilioninae.__str__(), 'Papilioninae')
    
    def test_subfamily_belongs_to_family(self):
        subfamily_papilioninae = factories.SubfamilyFactory()
        self.assertEqual(subfamily_papilioninae.family.name, 'Papilionidae')

class TestTribeModel(TestCase):
    "Tests for Tribe Model"

    def test_tribe_subclasses_from_taxonomybase(self):
        self.assertTrue(issubclass(Tribe, TaxonomyBaseInfo))
    
    def test_tribe_str_equals_name(self):
        tribe_papilionini = factories.TribeFactory()
        self.assertEqual(tribe_papilionini.__str__(), 'Papilionini')
    
    def test_tribe_belongs_to_subfamily(self):
        tribe_papilionini = factories.TribeFactory()
        self.assertEqual(tribe_papilionini.subfamily.name, 'Papilioninae')

class TestGenusModel(TestCase):
    "Tests for Genus Model"

    def test_genus_subclasses_from_taxonomybase(self):
        self.assertTrue(issubclass(Genus, TaxonomyBaseInfo))
    
    def test_genus_str_equals_name(self):
        genus_papilio = factories.GenusFactory()
        self.assertEqual(genus_papilio.__str__(), 'Papilio')
    
    def test_genus_belongs_to_tribe(self):
        genus_papilio = factories.GenusFactory()
        self.assertEqual(genus_papilio.tribe.name, 'Papilionini')