from django.test import TestCase
from django.urls import reverse
from app.models import Fournisseur
from app.forms import FournisseurForm
from django.utils import timezone

class FournisseurCreateViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('fournisseur-add')
        Fournisseur.objects.create(name='Existing Fournisseur', code='TF123', email='existing@example.com')

    def test_fournisseur_create_view_get(self):
        """Test que la vue renvoie le formulaire de création de fournisseur."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')
        self.assertIn('form', response.context)

    def test_fournisseur_create_view_post_invalid(self):
        """Test que la création d'un fournisseur échoue avec des données invalides."""
        response = self.client.post(self.url, {
            'name': '',  # Nom vide pour simuler une erreur de validation
            'code': 'TF123',  # Assurez-vous que ce code est unique
            'email': 'invalid-email',  # Email invalide
            'date_creation': '',  # Date de création vide
        })

        self.assertEqual(response.status_code, 200)
        
    def test_fournisseur_create_view_post_form_valid(self):
        """Test que la méthode form_valid redirige correctement après la création d'un fournisseur."""
        form_data = {
            'name': 'Test Fournisseur',
            'code': 'TF124',  # Assurez-vous que ce code est unique
            'email': 'test@example.com',  # Email valide
            'date_creation': timezone.now(),  # Date de création actuelle
        }
        response = self.client.post(self.url, form_data)
        
        # Vérifiez que le fournisseur a été créé
        fournisseur = Fournisseur.objects.filter(code='TF124').first()
        self.assertIsNotNone(fournisseur, "Fournisseur should have been created")
        self.assertEqual(fournisseur.email, 'test@example.com')

    def test_fournisseur_create_view_post_with_email(self):
        """Test que la création d'un fournisseur avec un email valide fonctionne."""
        form_data = {
            'name': 'Test Fournisseur',
            'code': 'TF125',  # Assurez-vous que ce code est unique
            'email': 'test@example.com',  # Email valide
            'status': 0,  # Utilisez une valeur valide pour le statut
            'date_creation': timezone.now(),  # Date de création actuelle
        }
        response = self.client.post(self.url, form_data)
        
        # Vérifiez que le fournisseur a été créé
        fournisseur = Fournisseur.objects.filter(code='TF125').first()
        self.assertIsNotNone(fournisseur, "Fournisseur should have been created")
        self.assertEqual(fournisseur.email, 'test@example.com')