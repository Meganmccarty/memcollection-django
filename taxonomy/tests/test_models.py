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