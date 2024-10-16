from django.test import TestCase
from django.utils import timezone
from app.models import Product, ProductItem

class ProductItemTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="T-Shirt",
            code="TS001",
            status=1,
            date_creation=timezone.now(),
        )
        self.product_item = ProductItem.objects.create(
            color="Red",
            code="TS001-RD",
            product=self.product
        )

    def test_product_item_str(self):
        """Test la méthode __str__ de ProductItem."""
        self.assertEqual(str(self.product_item), "Red TS001-RD")
