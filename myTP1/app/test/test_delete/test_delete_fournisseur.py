from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Fournisseur

class FournisseurDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.fournisseur = Fournisseur.objects.create(
            name="Test Fournisseur",
            code="TF123",
            email="test@example.com",
            phone="1234567890",
            address="123 Test St",
            website="http://example.com"
        )
        self.client.login(username='testuser', password='12345')

    def test_delete_fournisseur(self):
        response = self.client.post(reverse('fournisseur-delete', kwargs={'pk': self.fournisseur.pk}))
        self.assertRedirects(response, reverse('fournisseur-list'))
        self.assertFalse(Fournisseur.objects.filter(pk=self.fournisseur.pk).exists())

    def test_delete_fournisseur_context(self):
        response = self.client.get(reverse('fournisseur-delete', kwargs={'pk': self.fournisseur.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_total.html')
        self.assertEqual(response.context['titremenu'], 'fournisseur')