from django.test import TestCase, Client
from django.contrib.auth.models import User
from imager_images.models import Photo, Albums
from sorl.thumbnail import get_thumbnail
import factory

# Create your tests here.
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'password',)


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo
        django_get_or_create = ('profile', 'published', 'image',)

class AlbumsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Albums
        django_get_or_create = ('profile', 'published', 'cover', 'photos',)

class TestProfileViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bob = User.objects.create_user('bob')
        self.bob.set_password('test')
        self.bob.save()
        
        self.p = PhotoFactory(profile=self.bob.profile, published='pub', image='test.jpg')
        self.p.save()

    def test_profile_unsuccess(self):
        response = self.client.get('/profile/', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_profile_success(self):
        # tried factory and didn't work
        self.client.login(username='bob', password='test')
        response = self.client.get('/profile/', follow=True)
        self.assertTemplateUsed(response, 'profile.html')

    def test_no_cover(self):
        self.client.login(username='bob', password='test')
        response = self.client.get('/profile/', follow=True)
        self.assertIn('/media/photos/test/packman_2.jpg', response.content)

    def test_cover(self):
        self.bob.profile.picture = self.p.image
        self.bob.profile.save()
        self.client.login(username='bob', password='test')
        response = self.client.get('/profile/', follow=True)
        self.assertIn('test.jpg', response.content)

class TestStream(TestCase):

    def setUp(self):
        self.client = Client()
        self.bob = User.objects.create_user('bob')
        self.bob.set_password('test')
        self.bob.save()
        self.a = PhotoFactory(profile=self.bob.profile, published='pub', image='a.jpg')
        self.a.save()
        self.sally = User.objects.create_user('sally')
        self.sally.set_password('test')
        self.sally.save()
        self.b = PhotoFactory(profile=self.bob.profile, published='pub', image='b.jpg')
        self.b.save()

    def test_stream_view(self):
        self.client.login(username='bob', password='test')
        response = self.client.get('/stream/', follow=True)
        im = get_thumbnail(self.a.image.url, "400x400", crop="center")
        self.assertIn(im.url, response.content)

    def test_stream_follow_and_block(self):
        self.bob.profile.follow(self.sally.profile)
        self.client.login(username='bob', password='test')
        response = self.client.get('/stream/', follow=True)
        im = get_thumbnail(self.b.image.url, "400x400", crop="center")
        self.assertIn(im.url, response.content)
        self.sally.profile.block(self.bob.profile)
        response = self.client.get('/stream/', follow=True)
        self.assertNotIn(im.url, response.content)

class TestLibrary(TestCase): 
    def setUp(self):
        self.client = Client()
        self.bob = User.objects.create_user('bob')
        self.bob.set_password('test')
        self.bob.save()
        self.a = PhotoFactory(profile=self.bob.profile, published='pub', image='a.jpg')
        self.a.save()
        self.b = PhotoFactory(profile=self.bob.profile, published='pub', image='b.jpg')
        self.c = AlbumsFactory(profile=self.bob.profile, publish='pub', cover=self.a, photos=[self.a, self.b])
        self.b.save()
        self.c.save()

    def test_library(self):
        self.client.login(username='bob', password='test')
        response = self.client.get('/library/', follow=True)
        im = get_thumbnail(self.a.image.url, "400x400", crop="center")
        self.assertIn(im.url, response.content)

    def test_l_albums(self):
        self.client.login(username='bob', password='test')
        response = self.client.get('/library/', follow=True)
        im = get_thumbnail(self.c.cover.image.url, "400x400", crop="center")
        self.assertIn(im.url, response.content)
