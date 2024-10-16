from django.test import TestCase
from app.models import ProductAttribute

class ProductAttributeTestCase(TestCase):

    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name="Color")

    def test_product_attribute_creation(self):
        """Test la création d'un attribut produit."""
        self.assertEqual(self.attribute.name, "Color")

    def test_product_attribute_str(self):
        """Test la méthode __str__ de ProductAttribute."""
        self.assertEqual(str(self.attribute), "Color")
