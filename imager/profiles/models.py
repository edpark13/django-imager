from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class ActiveProfileManager(models.Manager):
    """
    A manager called when active is called in ImagerProfile 

    return a list of active ImagerProfile
    """
    def get_queryset(self):
        # calls default method with super
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """ImagerProfile class with instances that we want in a image app"""
    picture = models.ImageField(
        upload_to='profile_images',
        height_field='100px',
        width_field='100px',
        blank=True)
    user = models.OneToOneField(User, related_name='profile')
    phone = models.IntegerField(max_length=11, null=True)
    birthday = models.DateField(null=True)
    picture_privacy = models.BooleanField(default=True)
    phone_privacy = models.BooleanField(default=True)
    birthday_privacy = models.BooleanField(default=True)
    name_privacy = models.BooleanField(default=True)
    email_privacy = models.BooleanField(default=True)
    following = models.ManyToManyField('ImagerProfile', symmetrical=False,
                                       related_name='followers')
    block = models.ManyToManyField('ImagerProfile', symmetrical=True,
                                   related_name='+')

    def __str__(self):
        return self.user.username

    def is_active(self):
        return self.user.is_active

    objects = models.Manager()
    active = ActiveProfileManager()

    def follow(self, other_profile):
        """Defines this user as following other_profile."""
        self.following.add(other_profile)

    def unfollow(self, other_profile):
        self.following.remove(other_profile)

    def block(self, other_profile):
        self.block.add(other_profile)
        self.following.remove(other_profile)

    def unblocked_followers():
        self.block.remove(other_profile)








