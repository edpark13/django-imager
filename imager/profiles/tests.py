from django.test import TestCase
import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'john'

class Test_ImagerProfile(TestCase):
    def setUp(self):
        self.usertest = UserFactory.create()

    def test_create(self):
        assert self.usertest.ImagerProfile
