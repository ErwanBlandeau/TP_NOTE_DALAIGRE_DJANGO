from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import ProductAttribute
from app.views import ProductAttributeDeleteView

class ProductAttributeDeleteViewTest(TestCase):
    def setUp(self):
        # Create a user and log in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        
        # Create a ProductAttribute instance
        self.product_attribute = ProductAttribute.objects.create(name='Test Attribute')
    
    def test_delete_product_attribute(self):
        # Get the URL for the delete view
        url = reverse('product-attribute-delete', args=[self.product_attribute.id])
        
        # Send a POST request to delete the product attribute
        response = self.client.post(url)
        
        # Check that the response redirects to the product list
        self.assertRedirects(response, reverse('product-list'))
        
        # Check that the product attribute was deleted
        self.assertFalse(ProductAttribute.objects.filter(id=self.product_attribute.id).exists())

    def test_get_context_data(self):
        # Get the URL for the delete view
        url = reverse('product-attribute-delete', args=[self.product_attribute.id])
        
        # Send a GET request to retrieve the context data
        response = self.client.get(url)
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that 'titremenu' is in the context and has the correct value
        self.assertIn('titremenu', response.context)
        self.assertEqual(response.context['titremenu'], 'attribut')