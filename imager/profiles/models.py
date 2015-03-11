from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q
from imager_images.models import Photo, Albums

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
        upload_to='photos/test', null=True, blank=True, default='photos/test/packman_2.jpg')
    user = models.OneToOneField(User, related_name='profile')
    phone = models.IntegerField(max_length=11, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    picture_privacy = models.BooleanField(default=True)
    phone_privacy = models.BooleanField(default=True)
    birthday_privacy = models.BooleanField(default=True)
    name_privacy = models.BooleanField(default=True)
    email_privacy = models.BooleanField(default=True)
    following = models.ManyToManyField('ImagerProfile', symmetrical=False,
                                       related_name='_followers', null=True,
                                       blank=True)
    blocking = models.ManyToManyField('ImagerProfile', symmetrical=False,
                                      related_name='blockers', null=True,
                                      blank=True)

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
        """Removes passed user from relations table"""
        self.following.remove(other_profile)

    def block(self, other_profile):
        """Updates blocking column to capture that a user is blocking input
        user profile - does not change other column data"""
        self.blocking.add(other_profile)

    def unblock(self, other_profile):
        """Updates blocking column to capture that a user is no-longer
        blocking input user profile - does not change other column data"""
        self.blocking.remove(other_profile)

    def followers(self):
        """Lits all followers who are not currently blocked in the
        relationship table"""
        return ImagerProfile.objects.filter(Q(following=self) & ~Q(blockers=self) & ~Q(blocking=self))

    def get_unblock_following(self):
        return ImagerProfile.objects.filter(Q(_followers=self) & ~Q(blockers=self) & ~Q(blocking=self))

    # def create_photo(self):
        # Might need for photo creation at a future point
        # imager_images.Photo().save()

    def view_photos(self):
        """Photos that the user can view"""
        return Photo.objects.filter(profile=self)

    def view_albums(self):
        return Albums.objects.filter(profile=self)

    def view_others_photo(self, other):
        if self not in other.followers():
            return 'You are not following them'
        elif self in other.followers():
            return Photo.objects.filter(Q(published='pub') | Q(published='sha'))

    def num_of_photos(self):
        return len(self.photos.all())

    def num_of_albums(self):
        return len(self.albums.all())

    def get_profile_stream(self):
        return Photo.objects.filter(profile=self).order_by('date_uploaded').all()

    def get_followers_stream(self):
        followers = self.get_unblock_following()
        l = []
        for f in followers:
            l.append(f.photos.filter(Q(published='pub')))
        return l
