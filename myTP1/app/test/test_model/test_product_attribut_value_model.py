from django.test import TestCase
from app.models import ProductAttribute, ProductAttributeValue

class ProductAttributeValueTestCase(TestCase):

    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name="Color")
        self.attribute_value = ProductAttributeValue.objects.create(
            value="Red", 
            product_attribute=self.attribute,
            position=1
        )

    def test_product_attribute_value_creation(self):
        """Test la création d'une valeur d'attribut produit."""
        self.assertEqual(self.attribute_value.value, "Red")
        self.assertEqual(self.attribute_value.position, 1)

    def test_product_attribute_value_str(self):
        """Test la méthode __str__ de ProductAttributeValue."""
        self.assertEqual(str(self.attribute_value), "Red [Color]")
