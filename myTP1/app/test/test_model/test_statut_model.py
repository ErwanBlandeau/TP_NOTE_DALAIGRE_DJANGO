from django.test import TestCase
from app.models import Status

class StatusTestCase(TestCase):

    def setUp(self):
        self.status = Status.objects.create(numero=1, libelle="En stock")

    def test_status_str(self):
        """Test la méthode __str__ de Status."""
        self.assertEqual(str(self.status), "1 En stock")
