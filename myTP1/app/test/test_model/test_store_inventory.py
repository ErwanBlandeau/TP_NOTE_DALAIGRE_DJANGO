from django.test import TestCase
from django.utils import timezone
from app.models import Product, Fournisseur, StoreInventory

class StoreInventoryTestCase(TestCase):

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
            email="supplierA@example.com"
        )
        self.store_inventory = StoreInventory.objects.create(
            product=self.product,
            fournisseur=self.fournisseur,
            quantity_in_stock=50,
            price_in_store=22.99
        )

    def test_store_inventory_creation(self):
        """Test la création d'un inventaire en magasin."""
        self.assertEqual(self.store_inventory.product, self.product)
        self.assertEqual(self.store_inventory.quantity_in_stock, 50)

    def test_store_inventory_str(self):
        """Test la méthode __str__ de StoreInventory."""
        self.assertEqual(str(self.store_inventory), "T-Shirt fournit T-Shirt (Prix: 22.99 , Quantite: 50)")
