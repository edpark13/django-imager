from django.db import models
from django.utils.encoding import python_2_unicode_compatible

privacy_choices = (('public', 'public'),
           ('private', 'private'),
           ('shared', 'shared'))


@python_2_unicode_compatible
class Photo(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_choices,
                                 default='private')
    profile = models.ForeignKey('profile.ImagerProfile',
                                symetrical=True, related_name='photos')

    def __str__(self):
        return self.pk

@python_2_unicode_compatible
class Albums(models.Model):
    profile = models.ForeignKey('profile.ImagerProfile')
    photos = models.ManyToManyField('Photo', symetrical=True,
                                    related_name='album')
    title = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_choices,
                                 default='private')
    cover = models.ForeignKey('Photo', null=True, blank=True)

    def __str__(self):
        return self.pk

    pass
