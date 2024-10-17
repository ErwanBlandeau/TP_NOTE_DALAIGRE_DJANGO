from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Product, Fournisseur, ProductFournisseur
from django.utils import timezone

class ProductFournisseurDeleteViewTest(TestCase):
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
        self.product = Product.objects.create(
            name="Test Product",
            code="TP123",
            status=0,
            date_creation=timezone.now()
        )
        self.product_fournisseur = ProductFournisseur.objects.create(
            product=self.product,
            fournisseur=self.fournisseur,
            prix_fournisseur=100.00
        )
        self.client.login(username='testuser', password='12345')

    # def test_delete_product_fournisseur(self):
    #     response = self.client.post(reverse('each-fournisseur-product-update', kwargs={'pk': self.product_fournisseur.pk}))
    #     self.assertRedirects(response, reverse('each-fournisseur-product-list', kwargs={'pk': self.fournisseur.pk}))
    #     self.assertFalse(ProductFournisseur.objects.filter(pk=self.product_fournisseur.pk).exists())

    def test_delete_product_fournisseur_context(self):
        response = self.client.get(reverse('each-fournisseur-product-update', kwargs={'pk': self.product_fournisseur.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], 'modifier un produit du fournisseur')