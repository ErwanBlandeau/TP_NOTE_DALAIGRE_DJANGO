from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from app.admin import ProductItemAdmin, set_product_online, set_product_offline
from app.models import Product
from django.utils import timezone

class MockRequest:
    pass

class ProductAdminActionsTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.product_online = Product.objects.create(
            name="T-Shirt",
            code="TS001",
            status=1,
            date_creation=timezone.now(),
        )
        self.product_offline = Product.objects.create(
            name="Sweater",
            code="SW001",
            status=0,
            date_creation=timezone.now(),
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
