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