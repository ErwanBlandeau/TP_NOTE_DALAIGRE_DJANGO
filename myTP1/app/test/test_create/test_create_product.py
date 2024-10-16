from django.test import TestCase
from django.urls import reverse
from app.models import Product
from app.forms import ProductForm
from django.utils import timezone

class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('product-add')

    def test_product_create_view_get(self):
        """Test que la vue renvoie le formulaire de création de produit."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')
        self.assertIn('form', response.context)

    def test_product_create_view_post_success(self):
        """Test que la création d'un produit réussit avec des données valides."""
        response = self.client.post(self.url, {
            'name': 'Test Product',
            'code': 'TP123',  # Assurez-vous que ce code est unique
            'status': 0,  # Utilisez une valeur valide pour le statut
            'date_creation': timezone.now(),  # Date de création actuelle
        })
        
        self.assertRedirects(response, reverse('product-detail', args=[1]))  # Changez 1 par l'ID du produit créé
        self.assertTrue(Product.objects.filter(name='Test Product').exists())

    def test_product_create_view_post_invalid(self):
        """Test que la création d'un produit échoue avec des données invalides."""
        response = self.client.post(self.url, {
            'name': '',  # Nom vide pour simuler une erreur de validation
            'code': 'TP123',  # Assurez-vous que ce code est unique
            'status': -1,  # Statut invalide
            'date_creation': '',  # Date de création vide
        })

        self.assertEqual(response.status_code, 200)

