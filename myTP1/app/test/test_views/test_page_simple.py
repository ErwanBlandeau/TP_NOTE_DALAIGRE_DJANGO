from django.test import TestCase
from django.urls import reverse
from django.core import mail

class SimplePageTests(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home_no_param'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")
        self.assertTemplateUsed(response, 'simplePage.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About us...")
        self.assertTemplateUsed(response, 'simplePage.html')

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact us !")
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_valid(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('email-sent'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Message from Test User via MonProjet Contact Us form')

    def test_contact_view_post_invalid(self):
        response = self.client.post(reverse('contact'), {
            'name': '',
            'email': 'invalid-email',
            'message': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact us !")
        self.assertTemplateUsed(response, 'contact.html')

    def test_home_param_view(self):
        response = self.client.get(reverse('home', kwargs={'param': 'World'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello World")
        self.assertTemplateUsed(response, 'simplePage.html')

    def test_email_sent_view(self):
        response = self.client.get(reverse('email-sent'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email Sent Successfully!")
        self.assertTemplateUsed(response, 'email_sent.html')


class HomeParamViewTests(TestCase):
    def test_home_param_view(self):
        response = self.client.get(reverse('home', kwargs={'param': 'Test'}))  # Modifiez le nom de l'URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'simplePage.html')
        self.assertContains(response, "Hello Test")


class EmailSentViewTests(TestCase):
    def test_email_sent_view(self):
        response = self.client.get(reverse('email-sent'))  # Assurez-vous que 'email-sent' est le nom de votre URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'email_sent.html')
        self.assertContains(response, "Email Sent")
