from django.test import TestCase
from django.contrib.auth.models import User
from  django.urls import reverse

# Create your tests here.
class UserRegistrationTest(TestCase):

    def test_registration_view(self):
        response =self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testname').exists())

class UserLoginTest(TestCase):
    
    def setUp(self):
        self.user =User.objects.create_user(username='testname', password='testpassword123')
    
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication.login.html')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.client.session['_auth_user_id'])

class UserLogoutTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testname', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

    def test_user_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)