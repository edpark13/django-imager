from django.test import TestCase
import factory
from django.contrib.auth.models import User
from profiles.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'john'

class Test_ImagerProfile(TestCase):
    def setUp(self):
        self.usertest = UserFactory()

    def test_create(self):
        assert self.usertest.username == 'john'
        assert type(self.usertest) is User
        assert type(self.usertest.profile) is ImagerProfile

    def test_delete(self):
        self.sally = UserFactory(username='sally')
        assert self.sally.profile in ImagerProfile.objects.all()
        self.sally.delete()
        assert self.sally.profile not in ImagerProfile.objects.all()

    # def test_is_active(self):
