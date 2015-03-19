from django.test import TestCase, Client
from django.contrib.auth.models import User
from imager_images.models import Photo
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo
        django_get_or_create = ('profile', 'published', 'image',)

    
class TestHomepageViews(TestCase):

    def setUp(self):
        self.bob = UserFactory(username='bob').profile

    def test_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_default_photo(self):
        response = self.client.get('/')
        self.assertEqual(response.context['picture'], None)

    def test_random_photo(self):
        self.bobimage = PhotoFactory(profile=self.bob, published='pub', image='bob.jpg')
        response = self.client.get('/')
        self.assertEqual(response.context['picture'].image, self.bobimage.image)


class TestRegistration(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_page_works(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        self.client.post('/accounts/register/',
                         {'username': 'bob',
                          'email': 'bob@example.com',
                          'password1': 'test',
                          'password2': 'test'})
        self.assertEqual(len(User.objects.all()), 1)

class TestLoginandLogout(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_page_works(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/accounts/login/',follow=True)
        self.client.post('/accounts/login/',
                         {'username': 'bob',
                          'password': 'test'})
        self.assertEqual(response.status_code, 200)


    def test_logout(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)



