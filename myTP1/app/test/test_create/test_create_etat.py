from django.test import TestCase
from django.urls import reverse
from django.forms.models import model_to_dict
from app.models import Etat
from app.forms import EtatForm

class EtatCreateViewTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'nomEtat': 'En cours'
        }
        self.invalid_data = {
            'nomEtat': ''
        }

    def test_etat_create_view_get(self):
        response = self.client.get(reverse('etat-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_etat.html')
        self.assertIsInstance(response.context['form'], EtatForm)

    def test_etat_create_view_post_valid(self):
        response = self.client.post(reverse('etat-add'), data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Etat.objects.filter(nomEtat='En cours').exists())

    def test_etat_create_view_post_invalid(self):
        response = self.client.post(reverse('etat-add'), data=self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_etat.html')
        self.assertFalse(Etat.objects.filter(nomEtat='').exists())