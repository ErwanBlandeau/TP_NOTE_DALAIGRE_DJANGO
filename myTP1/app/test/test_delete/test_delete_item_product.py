from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import ProductItem, Product

class ProductItemDeleteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product')
        self.product_item = ProductItem.objects.create(color='Red', code='123', product=self.product)
        self.url = reverse('product-item-delete', args=[self.product_item.id])

    def test_delete_product_item_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_total.html')
        self.assertContains(response, 'item')

    def test_delete_product_item(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('product-list'))
        self.assertFalse(ProductItem.objects.filter(id=self.product_item.id).exists())

    def test_delete_product_item_not_logged_in(self):
        response = self.client.post(self.url)
        self.assertNotEqual(response.status_code, 200)
        self.assertFalse(ProductItem.objects.filter(id=self.product_item.id).exists())