from django.test import TestCase
from django.utils import timezone
from app.models import Product
from django.db import IntegrityError  

class ProductTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="T-Shirt", 
            code="TS001",
            price_ht=19.99,
            price_ttc=23.99,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )

    def test_product_creation(self):
        """Test la création d'un produit."""
        self.assertEqual(self.product.name, "T-Shirt")
        self.assertEqual(self.product.code, "TS001")

    def test_product_str(self):
        """Test la méthode __str__ de Product."""
        self.assertEqual(str(self.product), "T-Shirt TS001")

    def test_product_unique_code(self):
        """Test que le code du produit est unique."""
        with self.assertRaises(IntegrityError):
            Product.objects.create(name="Sweater", code="TS001")
