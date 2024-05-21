from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(user=self.user, content='a test post')

    def test_post_creation(self):
        self.assertEqual(self.post.user.username, 'testuser')
        self.assertEqual(self.post.content, 'a test post')

class PostViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        Post.objects.create(user=self.user, content='a test post')

    def test_create_post(self):
        response = self.client.post('/post/create/', {'content': 'Another test post'})
        self.assertRedirects(response, '/')
        self.assertEqual(Post.objects.count(), 2)

    def test_view_posts(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a test post')