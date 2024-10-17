from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Product, Fournisseur, ProductFournisseur

class ProductFournisseurCreateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.product = Product.objects.create(name="Test Product", code="TP001")
        self.fournisseur = Fournisseur.objects.create(name="Test Fournisseur", code="TF001", email="test@example.com")

    def test_create_product_fournisseur(self):
        url = reverse('each-fournisseur-product-add', kwargs={'pk': self.fournisseur.pk})
        data = {
            'product': self.product.id,
            'fournisseur': self.fournisseur.id,
            'prix_fournisseur': '100.00'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ProductFournisseur.objects.filter(product=self.product, fournisseur=self.fournisseur).exists())

    def test_create_product_fournisseur_invalid_data(self):
        url = reverse('each-fournisseur-product-add', kwargs={'pk': self.fournisseur.pk})
        data = {
            'product': '',
            'fournisseur': '',
            'prix_fournisseur': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_create_product_fournisseur_duplicate(self):
        ProductFournisseur.objects.create(product=self.product, fournisseur=self.fournisseur, prix_fournisseur='100.00')
        url = reverse('each-fournisseur-product-add', kwargs={'pk': self.fournisseur.pk})
        data = {
            'product': self.product.id,
            'fournisseur': self.fournisseur.id,
            'prix_fournisseur': '150.00'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_get_context_data(self):
        url = reverse('each-fournisseur-product-add', kwargs={'pk': self.fournisseur.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ajouter un nouveau produit au fournisseur")