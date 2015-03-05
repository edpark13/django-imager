from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from models import ImagerProfile

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """When creating a new User also create a new ImagerProfile"""
    if kwargs.get('created', False):
        ImagerProfile(user=kwargs.get('instance')).save()


@receiver(pre_delete, sender=User)
def delete_profile(sender, **kwargs):
    """When a User is deleted, delete the corresponding ImagerProfile"""
    ImagerProfile.objects.get(user=kwargs.get('instance')).delete()
