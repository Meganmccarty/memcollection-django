from django.test import TestCase
from taxonomy.models import *

class OrderTest(TestCase):
    @classmethod
    def setUp(self):
        Order.objects.create(name='Test Order', common_name='Test Common Name', authority='Test Authority')
    
    def test_subclasses_model_base(self):
        self.assertTrue(issubclass(Order, TaxonomyBaseInfo))
    
    def test_model_str(self):
        taxon = Order.objects.get(id=1)
        self.assertEqual(str(taxon), 'Test Order')
