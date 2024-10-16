# from django.test import TestCase
# from django.urls import reverse
# from app.models import Commande, Product, Fournisseur, ProductFournisseur
# from django.contrib.auth.models import User




# class CommandeCreateViewTestCase(TestCase):
#     def setUp(self):
#         self.url = reverse('commande-create')
#         self.user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
#         self.client.login(username='testuser', password='12345')
#         self.produit = Product.objects.create(name='Test Product', code='TP001', status=0, date_creation='2023-01-01')
#         self.fournisseur = Fournisseur.objects.create(name='Test Fournisseur', code='TF001', email='test@example.com', phone='1234567890', address='123 Test St', website='http://example.com')
#         ProductFournisseur.objects.create(product=self.produit, fournisseur=self.fournisseur)

#     def test_commande_create_view_get(self):
#         """Test que la vue renvoie le formulaire de création de commande."""
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 302)
#         self.assertIn('form', response.context)

#     def test_commande_create_view_get_with_produit_id(self):
#         """Test que la vue renvoie la liste des fournisseurs pour un produit donné."""
#         response = self.client.get(self.url, {'produit_id': self.produit.id})
#         self.assertEqual(response.status_code, 302)
#         self.assertJSONEqual(response.content, [{'id': self.fournisseur.id, 'name': self.fournisseur.name}])
