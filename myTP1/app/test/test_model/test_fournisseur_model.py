from django.test import TestCase
from app.models import Fournisseur
from django.db import IntegrityError
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
