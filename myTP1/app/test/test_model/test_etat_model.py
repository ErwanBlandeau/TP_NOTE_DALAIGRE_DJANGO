from django.test import TestCase
from app.models import Etat

class EtatTestCase(TestCase):

    def setUp(self):
        self.etat = Etat.objects.create(nomEtat="En attente")

    def test_etat_str(self):
        """Test la méthode __str__ de Etat."""
        self.assertEqual(str(self.etat), "En attente")
