from django.test import TestCase
import factory
from django.contrib.auth.models import User
from profiles.models import ImagerProfile
from imager_images.models import Photo, Albums
import datetime


class UserFactory(factory.django.DjangoModelFactory):
    """Creates a test user not: non permante to db"""
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'john'

class Test_ImagerProfile(TestCase):
    def setUp(self):
        """Creats the User defined in UserFactory"""
        self.usertest = UserFactory()
        self.johnny = UserFactory(username='johnny').profile
        self.may = UserFactory(username='may').profile
        self.dave = UserFactory(username='dave').profile
        self.sally = UserFactory(username='sally').profile

    def test_create(self):
        """Test that a profile is created with a User creation"""
        assert self.usertest.username == 'john'
        type(self.usertest) is User
        assert type(self.usertest.profile) is ImagerProfile

    def test_delete(self):
        """Test that a profile is delted when a User is delted"""
        self.sally = UserFactory(username='sally')
        assert self.sally.profile in ImagerProfile.objects.all()
        self.sally.delete()
        assert self.sally.profile not in ImagerProfile.objects.all()

    def test_active(self):
        """Test that a newly created profile is defaulting to active"""
        assert self.usertest.profile in ImagerProfile.active.all()

    def test_inactive(self):
        """Test that changing a user to inactive also makes the profile
        inactive"""
        self.usertest.is_active = False
        self.usertest.save()
        ImagerProfile.active.all()
        assert self.usertest.profile not in ImagerProfile.active.all()

    def test_reactivate(self):
        """Test that changing a user to active also makes the profile
        active"""
        self.usertest.is_active = True
        self.usertest.save()
        assert self.usertest.is_active is True

    def test_follow(self):
        """Test that one user can follow other users"""
        assert len(self.dave.following.all()) == 0
        self.dave.follow(self.sally)
        assert self.sally in  \
            self.dave.following.filter(user=self.sally)

    def test_following(self):
        """Test that the list of a users followers is corretnly returned"""
        self.johnny.follow(self.may)
        assert self.johnny in self.may._followers.all()

    def test_unfollow(self):
        """Test that a user can terminate a follow connection"""
        self.johnny.follow(self.may)
        self.johnny.unfollow(self.may)
        assert len(self.johnny.following.all()) == 0
        assert len(self.may._followers.all()) == 0

    def test_block(self):
        """Test that a user can initate a block relationship while not
        affecting other relationships"""
        self.dave.follow(self.johnny)
        self.may.follow(self.johnny)
        self.johnny.follow(self.may)
        self.johnny.block(self.may)
        assert self.may in self.johnny.blocking.all()
        assert self.may not in self.johnny.followers().all()
        assert self.may in self.johnny._followers.all()
        assert self.dave in self.johnny.followers().all()

    def test_unblock(self):
        """Test that a user can terminate a block relationship while not
        affecting other relationships"""
        self.johnny.follow(self.may)
        self.may.follow(self.johnny)
        self.johnny.block(self.may)
        assert self.may in self.johnny.blocking.all()
        self.johnny.unblock(self.may)
        assert self.may not in self.johnny.blocking.all()
        assert self.may in self.johnny.followers()

###########################
# Testing Images
###########################


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
        django_get_or_create = ('profile', 'published',)

    # image = factory.django.ImageField(color='blue')
    profile = UserFactory.create().profile
    published = 'pub'


class Test_Photo(TestCase):
    def setUp(self):
        self.photo = PhotoFactory.create(title='test', description='test photo')

    def test_view_photos(self):
        assert self.photo.title == 'test'
        assert self.photo.description == 'test photo'

    def test_photo_dates(self):
        assert self.photo.date_uploaded == datetime.date.today()
        assert self.photo.date_published == datetime.date.today()
        assert self.photo.date_modified == datetime.date.today()

    def test_viewphoto(self):
        assert self.photo in self.photo.profile.view_photos().all()


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Albums
        django_get_or_create = ('profile', 'published',)
    # profile = UserFactory.create().profile
    published = 'pub'


class Test_Album(TestCase):
    def setUp(self):
        self.user = UserFactory(username='john').profile
        self.album = AlbumFactory.create(profile=self.user,
                                         title='album',
                                         description='Test Album')
        self.photo = PhotoFactory.create(profile=self.user,
                                         title='test', 
                                         description='test photo')

    def test_add_photo(self):
        """Add a photo to a album."""
        assert len(self.album.photos.all()) == 0
        assert self.album.profile == self.photo.profile
        self.album.photos.add(self.photo)
        assert self.photo in self.album.photos.all()
    
    def test_view_albums(self):
        assert self.album in self.user.view_albums().all()

    def test_cover(self):
        assert self.album.cover is None
        self.album.cover = self.photo
        assert self.album.cover == self.photo

    def test_view_other_photo(self):
        self.bob = UserFactory(username='bob').profile
        self.bob.follow(self.user)
        assert self.bob in self.user.followers().all()
        assert self.photo in self.bob.view_others_photo(self.user).all()
        self.user.block(self.bob)
        assert 'You are not following them' == self.bob.view_others_photo(self.user)
