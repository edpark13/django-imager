from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible


class ActiveProfileManager(models.Manager):
    """Inheriting et_queryset, return only active users."""
    def get_queryset(self):
        # calls default method with super
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    picture = models.ImageField(
        upload_to='profile_images',
        height_field='100px',
        width_field='100px',
        blank=True)
    user = models.OneToOneField(User, related_name='profile')
    phone = models.IntegerField(max_length=11)
    birthday = models.DateField()
    picture_privacy = models.BooleanField(default=True)
    phone_privacy = models.BooleanField(default=True)
    birthday_privacy = models.BooleanField(default=True)
    name_privacy = models.BooleanField(default=True)
    email_privacy = models.BooleanField(default=True)

    def __str__(self):
        return self.user

    def is_active(self):
        return self.user.is_active

    # # @classmethod
    # def active(cls):
    #     qs = cls.get_queryset()
    #     return qs.filter(user__is_active=True)

    objects = models.Manager()
    active = ActiveProfileManager()
