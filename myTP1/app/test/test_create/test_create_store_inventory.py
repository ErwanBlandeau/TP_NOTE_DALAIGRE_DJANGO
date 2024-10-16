from django.test import TestCase, Client
from django.urls import reverse
from app.models import StoreInventory
from app.models import Product

class StoreInventoryCreateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('each-market-inventory-add')

    def test_store_inventory_create_view_get(self):
        """Test que la vue renvoie le formulaire de création d'inventaire de magasin."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')

    def test_store_inventory_create_view_post_invalid(self):
        """Test que la création d'un inventaire de magasin échoue avec des données invalides."""
        response = self.client.post(self.url, {'product': ''})  # Invalid data
        self.assertEqual(response.status_code, 200)

    def test_store_inventory_create_view_post_success(self):
        """Test que la création d'un inventaire de magasin réussit avec des données valides."""
        response = self.client.post(self.url, {
            'name': 'Test Inventory',
            'quantity': 100,
        })
        self.assertEqual(response.status_code, 200)  # Redirect on success

        # Retrieve the created inventory
        # Assuming a Product instance already exists for the test
        product = Product.objects.create(name='Test Product')

        response = self.client.post(self.url, {
            'product': product.id,
            'quantity_in_stock': 100,
            'price_in_store': 9.99,
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success

        # Retrieve the created inventory
        inventory = StoreInventory.objects.get(product=product)
        
        # Assert the redirection to the inventory list view
        self.assertRedirects(response, reverse('each-market-inventory-list'))
        self.assertTrue(StoreInventory.objects.filter(product=product).exists())