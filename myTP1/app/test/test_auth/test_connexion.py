from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ConnectViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_successful_login(self):
        """Test successful login with correct credentials."""
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'simplePage.html')
        self.assertContains(response, f"hello "+self.username)

    def test_login_with_incorrect_credentials(self):
        """Test login with incorrect credentials."""
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_with_inactive_user(self):
        """Test login with an inactive user."""
        self.user.is_active = False
        self.user.save()
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class RegisterViewTestCase(TestCase):
    
    def test_register_view_success(self):
        """Test l'inscription d'un utilisateur avec des informations valides."""
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'mail': 'testuser@example.com',
            'password': 'testpassword123'
        })
        
        # Vérifier que l'utilisateur a été créé
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)
        
        # Vérifier que la réponse est 200 OK et que le bon template est utilisé
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')  # Vérifiez que vous êtes redirigé vers la page de connexion

    def test_register_view_failure(self):
        """Test l'inscription d'un utilisateur avec des informations invalides."""
        response = self.client.post(reverse('register'), {
            'username': '',  # Username vide pour déclencher une erreur
            'mail': 'invalid-email',  # Email invalide
            'password': ''  # Mot de passe vide
        })
        
        # Vérifier que la réponse est 200 OK et que le bon template est utilisé
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')  # Vérifiez que vous restez sur la page d'inscription


