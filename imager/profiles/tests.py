from django.test import TestCase
import factory
from django.contrib.auth.models import User
from profiles.models import ImagerProfile


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

