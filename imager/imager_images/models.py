from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published = models.CharField(choices=(
        ('public', 'public'),
        ('private', 'private'),
        ('shared', 'shared')), default='private')
    profile = models.ForeignField('ImagerProfile', symmetrical=True, related_name='photos')
    

class Albums(models.Model):
    pass
