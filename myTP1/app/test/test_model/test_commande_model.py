from django.test import TestCase
from django.utils import timezone
from app.models import Product, Fournisseur, Etat, Commande

class CommandeTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="T-Shirt", 
            code="TS001",
            status=1,
            date_creation=timezone.now(),
        )
        self.fournisseur = Fournisseur.objects.create(
            name="Supplier A",
            code="SUP001",
            email="supplierA@example.com"
        )
        self.etat = Etat.objects.create(nomEtat="En attente")
        self.commande = Commande.objects.create(
            produit=self.product,
            fournisseur=self.fournisseur,
            quantite_du_produit=10,
            etat=self.etat
        )

    def test_commande_creation(self):
        """Test la création d'une commande."""
        self.assertEqual(self.commande.produit, self.product)
        self.assertEqual(self.commande.fournisseur, self.fournisseur)
        self.assertEqual(self.commande.quantite_du_produit, 10)
        self.assertEqual(self.commande.etat, self.etat)

    def test_commande_str(self):
        """Test la méthode __str__ de Commande."""
        self.assertEqual(
            str(self.commande), 
            f"Commande de {self.product} par {self.fournisseur} le {self.commande.date_creation}"
        )