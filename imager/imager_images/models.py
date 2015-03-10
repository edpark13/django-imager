from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# from profiles.models import ImagerProfile

privacy_choices = (('pub', 'public'),
                   ('pri', 'private'),
                   ('sha', 'shared'))

def get_random_picture():
    return Photo.objects.filter(published='pub').all().order_by('?')[0]

@python_2_unicode_compatible
class Photo(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_choices,
                                 default='pri', max_length=4)
    profile = models.ForeignKey('profiles.ImagerProfile',
                                related_name='photos')

    def __str__(self):
        return str(self.pk)


@python_2_unicode_compatible
class Albums(models.Model):
    profile = models.ForeignKey('profiles.ImagerProfile')
    photos = models.ManyToManyField('Photo',
                                    related_name='album')
    title = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published = models.CharField(choices=privacy_choices,
                                 default='pri', max_length=4)
    cover = models.ForeignKey('Photo', null=True, blank=True)

    def __str__(self):
        return str(self.pk)

