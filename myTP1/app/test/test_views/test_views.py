from django.test import TestCase
from django.urls import reverse
from app.models import ProductAttribute, ProductAttributeValue, Product
from django.utils import timezone

class ProductAttributeDetailViewTestCase(TestCase):

    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name="Color")
        self.value1 = ProductAttributeValue.objects.create(
            value="Red", 
            product_attribute=self.attribute,
            position=1
        )
        self.value2 = ProductAttributeValue.objects.create(
            value="Blue", 
            product_attribute=self.attribute,
            position=2
        )

    def test_view_status_code(self):
        """Test that the view returns a 200 status code."""
        response = self.client.get(reverse('attribute-detail', args=[self.attribute.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_context_data_titremenu(self):
        """Test that the context contains 'titremenu'."""
        response = self.client.get(reverse('attribute-detail', args=[self.attribute.id]))
        self.assertEqual(response.context['titremenu'], "Détail attribut")

    def test_view_context_data_values(self):
        """Test that the context contains 'values' ordered by position."""
        response = self.client.get(reverse('attribute-detail', args=[self.attribute.id]))
        values = list(response.context['values'])
        self.assertEqual(values, [self.value1, self.value2])

class ProductDetailViewTestCase(TestCase):
    
    def setUp(self):
        # Créer un produit à tester
        self.product = Product.objects.create(
            name="T-Shirt",
            code="TS001",
            price_ht=20.00,
            price_ttc=30.00,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )

    def test_product_detail_view(self):
        """Test de la vue de détail du produit."""
        response = self.client.get(reverse('product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_product.html')
        self.assertEqual(response.context['product'], self.product)
        self.assertEqual(response.context['titremenu'], "Détail produit")
