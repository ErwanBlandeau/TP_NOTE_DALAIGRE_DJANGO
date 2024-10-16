from django.test import TestCase
from django.db import IntegrityError
from app.models import Product, Fournisseur, ProductFournisseur, StoreInventory, ProductAttribute, ProductAttributeValue, Etat, Commande
from django.utils import timezone

class ProductTestCase(TestCase):

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

    def test_product_creation(self):
        """Test la création d'un produit."""
        self.assertEqual(self.product.name, "T-Shirt")
        self.assertEqual(self.product.code, "TS001")

    def test_product_str(self):
        """Test la méthode __str__ de Product."""
        self.assertEqual(str(self.product), "T-Shirt TS001")

    def test_product_unique_code(self):
        """Test que le code du produit est unique."""
        with self.assertRaises(IntegrityError):
            Product.objects.create(name="Sweater", code="TS001")

class FournisseurTestCase(TestCase):

    def setUp(self):
        self.fournisseur = Fournisseur.objects.create(
            name="Supplier A",
            code="SUP001",
            email="supplierA@example.com",
            phone="1234567890",
            address="123 Supplier Street",
            website="http://www.supplierA.com"
        )

    def test_fournisseur_creation(self):
        """Test la création d'un fournisseur."""
        self.assertEqual(self.fournisseur.name, "Supplier A")

    def test_fournisseur_str(self):
        """Test la méthode __str__ de Fournisseur."""
        self.assertEqual(str(self.fournisseur), "Supplier A - SUP001")

    def test_fournisseur_unique_code(self):
        """Test que le code du fournisseur est unique."""
        with self.assertRaises(IntegrityError):
            Fournisseur.objects.create(name="Supplier B", code="SUP001")

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

class ProductAttributeTestCase(TestCase):

    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name="Color")

    def test_product_attribute_creation(self):
        """Test la création d'un attribut produit."""
        self.assertEqual(self.attribute.name, "Color")

    def test_product_attribute_str(self):
        """Test la méthode __str__ de ProductAttribute."""
        self.assertEqual(str(self.attribute), "Color")

class ProductAttributeValueTestCase(TestCase):

    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name="Color")
        self.attribute_value = ProductAttributeValue.objects.create(
            value="Red", 
            product_attribute=self.attribute,
            position=1
        )

    def test_product_attribute_value_creation(self):
        """Test la création d'une valeur d'attribut produit."""
        self.assertEqual(self.attribute_value.value, "Red")
        self.assertEqual(self.attribute_value.position, 1)

    def test_product_attribute_value_str(self):
        """Test la méthode __str__ de ProductAttributeValue."""
        self.assertEqual(str(self.attribute_value), "Red [Color]")

class CommandeTestCase(TestCase):

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


from app.models import Status, ProductItem, Etat

class StatusTestCase(TestCase):

    def setUp(self):
        self.status = Status.objects.create(numero=1, libelle="En stock")

    def test_status_str(self):
        """Test la méthode __str__ de Status."""
        self.assertEqual(str(self.status), "1 En stock")


class ProductItemTestCase(TestCase):

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
        self.product_item = ProductItem.objects.create(
            color="Red",
            code="TS001-RD",
            product=self.product
        )

    def test_product_item_str(self):
        """Test la méthode __str__ de ProductItem."""
        self.assertEqual(str(self.product_item), "Red TS001-RD")


class EtatTestCase(TestCase):

    def setUp(self):
        self.etat = Etat.objects.create(nomEtat="En attente")

    def test_etat_str(self):
        """Test la méthode __str__ de Etat."""
        self.assertEqual(str(self.etat), "En attente")
