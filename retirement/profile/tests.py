from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profiles

# Create your tests here.
class ProfilesModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profiles.objects.create(user=self.user, bio='a test bio')
    
    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'a test bio')

class ProfilesViewTest(TestCase):

    def setUP(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        Profiles.objects.create(user=self.user, bio='a test bio')

    def test_view_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'a test bio')

    def test_edit_profile(self):
        response = self.client.post('/profile/edit/', {'bio': 'Updated bio'})
        self.assertRedirects(response, '/profile/')
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.bio, 'Updated bio')
