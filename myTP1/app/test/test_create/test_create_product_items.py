from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import ProductItem, Product
from app.forms import ProductItemForm

class ProductItemCreateViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product')
        self.valid_data = {
            'color': 'Red',
            'code': 'R123',
            'product': self.product.id,
        }
        self.invalid_data = {
            'color': '',
            'code': 'R123',
            'product': self.product.id,
        }

    def test_create_product_item_view_success(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('product-item-add'), data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ProductItem.objects.filter(code='R123').exists())

    def test_create_product_item_view_failure(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('product-item-add'), data=self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ProductItem.objects.filter(code='R123').exists())