from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from app.models import Product

class ProductDeleteViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            code="TP001",
            status=1,
            date_creation=timezone.now()
        )
        self.delete_url = reverse('product-delete', kwargs={'pk': self.product.pk})

    def test_delete_product_view(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_total.html')
        self.assertContains(response, "Suppression d\'un produit")

    def test_post_delete_product(self):
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, reverse('product-list'))
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())