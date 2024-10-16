from django.test import TestCase
from django.urls import reverse
from django.forms.models import model_to_dict
from app.models import ProductAttribute

class ProductAttributeCreateViewTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Color'
        }
        self.invalid_data = {
            'name': ''  # Name is required, so this should be invalid
        }

    def test_create_product_attribute_valid(self):
        response = self.client.post(reverse('product-attribute-add'), data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(ProductAttribute.objects.filter(name='Color').exists())

    def test_create_product_attribute_invalid(self):
        response = self.client.post(reverse('product-attribute-add'), data=self.invalid_data)
        self.assertEqual(response.status_code, 200)  # Should return to the form with errors
        self.assertFalse(ProductAttribute.objects.filter(name='').exists())