from django.test import TestCase
from django.utils import timezone
from app.models import Product, Fournisseur, ProductFournisseur
from django.db import IntegrityError  
class ProductFournisseurTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="T-Shirt", 
            code="TS001",
            price_ht=19.99,
            price_ttc=23.99,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )
        self.fournisseur = Fournisseur.objects.create(
            name="Supplier A",
            code="SUP001",
            email="supplierA@example.com",
            phone="1234567890",
            address="123 Supplier Street",
            website="http://www.supplierA.com"
        )
        self.product_fournisseur = ProductFournisseur.objects.create(
            product=self.product,
            fournisseur=self.fournisseur,
            prix_fournisseur=15.99
        )

    def test_product_fournisseur_creation(self):
        """Test la création d'un lien entre un produit et un fournisseur."""
        self.assertEqual(self.product_fournisseur.product, self.product)
        self.assertEqual(self.product_fournisseur.fournisseur, self.fournisseur)
        self.assertEqual(self.product_fournisseur.prix_fournisseur, 15.99)

    def test_product_fournisseur_str(self):
        """Test la méthode __str__ de ProductFournisseur."""
        self.assertEqual(str(self.product_fournisseur), "Supplier A fournit T-Shirt (Prix: 15.99)")

    def test_product_fournisseur_unique(self):
        """Test que la relation entre un produit et un fournisseur est unique."""
        with self.assertRaises(IntegrityError):
            ProductFournisseur.objects.create(
                product=self.product,
                fournisseur=self.fournisseur,
                prix_fournisseur=15.99
            )
