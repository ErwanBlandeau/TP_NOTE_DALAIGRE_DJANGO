from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from app.admin import ProductAdmin, ProductItemAdmin, set_product_online, set_product_offline
from app.models import Product
from django.utils import timezone

class MockRequest:
    pass

class ProductAdminActionsTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.product_admin = ProductAdmin(Product, self.site)
        self.product_online = Product.objects.create(
            name="T-Shirt",
            code="TS001",
            price_ht=19.99,
            price_ttc=23.99,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )
        self.product_offline = Product.objects.create(
            name="Sweater",
            code="SW001",
            price_ht=29.99,
            price_ttc=35.99,
            status=0,
            date_creation=timezone.now(),
            nombre_de_produit=50
        )

    def test_set_product_online(self):
        """Test de l'action 'Mettre en ligne'."""
        queryset = Product.objects.filter(status=0)  # On ne prend que les produits hors ligne
        set_product_online(None, MockRequest(), queryset)
        self.product_offline.refresh_from_db()
        self.assertEqual(self.product_offline.status, 1)  # Vérifie que le produit est en ligne

    def test_set_product_offline(self):
        """Test de l'action 'Mettre hors ligne'."""
        queryset = Product.objects.filter(status=1)  # On ne prend que les produits en ligne
        set_product_offline(None, MockRequest(), queryset)
        self.product_online.refresh_from_db()
        self.assertEqual(self.product_online.status, 0)  # Vérifie que le produit est hors ligne

class ProductAdminInlinesTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.product_admin = ProductAdmin(Product, self.site)

    def test_inlines(self):
        """Test que ProductAdmin inclut ProductItemAdmin en tant qu'inline."""
        self.assertIn(ProductItemAdmin, self.product_admin.inlines)

class ProductAdminListDisplayTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.product_admin = ProductAdmin(Product, self.site)

    def test_list_display(self):
        """Test que les champs sont bien présents dans list_display de ProductAdmin."""
        self.assertEqual(
            self.product_admin.list_display, 
            ["code", "name", "price_ht", "price_ttc", "tax"]
        )

    def test_list_editable(self):
        """Test que les champs sont bien modifiables dans list_editable de ProductAdmin."""
        self.assertEqual(
            self.product_admin.list_editable, 
            ["name", "price_ht", "price_ttc"]
        )

class ProductAdminTaxCalculationTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.product_admin = ProductAdmin(Product, self.site)
        self.product = Product.objects.create(
            name="T-Shirt",
            code="TS001",
            price_ht=20.00,
            price_ttc=30.00,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )
        self.product_no_ht = Product.objects.create(
            name="Pants",
            code="PT001",
            price_ht=None,
            price_ttc=30.00,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )
        self.product_no_ttc = Product.objects.create(
            name="Cap",
            code="CP001",
            price_ht=10.00,
            price_ttc=None,
            status=1,
            date_creation=timezone.now(),
            nombre_de_produit=100
        )

    def test_tax_calculation(self):
        """Test du calcul des taxes lorsque price_ht et price_ttc sont définis."""
        self.assertEqual(self.product_admin.tax(self.product), 50.0)

    def test_tax_calculation_no_ht(self):
        """Test que la méthode tax retourne None si price_ht est None."""
        self.assertIsNone(self.product_admin.tax(self.product_no_ht))

    def test_tax_calculation_no_ttc(self):
        """Test que la méthode tax retourne None si price_ttc est None."""
        self.assertIsNone(self.product_admin.tax(self.product_no_ttc))
