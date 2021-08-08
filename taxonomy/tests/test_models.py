from django.test import TestCase
from taxonomy.models import *

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
    def test_subclasses_order_model_base(self):
        self.assertTrue(issubclass(Order, TaxonomyBaseInfo))
    
    def test_subclasses_family_model_base(self):
        self.assertTrue(issubclass(Family, TaxonomyBaseInfo))
    
    def test_subclasses_subfamily_model_base(self):
        self.assertTrue(issubclass(Subfamily, TaxonomyBaseInfo))
    
    def test_order_model_str(self):
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), 'Test Order Name')
    
    def test_family_model_str(self):
        family = Family.objects.get(id=1)
        self.assertEqual(str(family), 'Test Family Name')
    
    def test_subfamily_model_str(self):
        subfamily = Subfamily.objects.get(id=1)
        self.assertEqual(str(subfamily), 'Test Subfamily Name')