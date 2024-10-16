from django.test import TestCase
from django.urls import reverse
from app.models import Commande
from app.forms import CommandeForm

class CommandeCreateViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('commande-create')

    def test_commande_create_view_get(self):
        """Test que la vue renvoie le formulaire de création de commande."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_commande.html')
        self.assertIn('form', response.context)

    def test_commande_create_view_post_success(self):
        """Test que la création d'une commande réussit avec des données valides."""
        response = self.client.post(self.url, {
            'product': '1',  # Assurez-vous que ce produit existe
            'quantity': 10,
        })
        
        self.assertRedirects(response, reverse('commande-list'))
        self.assertTrue(Commande.objects.filter(product_id=1, quantity=10).exists())

    def test_commande_create_view_post_invalid(self):
        """Test que la création d'une commande échoue avec des données invalides."""
        response = self.client.post(self.url, {
            'product': '',  # Produit vide pour simuler une erreur de validation
            'quantity': -1,  # Quantité invalide
        })

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'product', 'This field is required.')
        self.assertFormError(response, 'form', 'quantity', 'Ensure this value is greater than or equal to 0.')
