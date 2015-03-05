from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from models import ImagerProfile

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        try:
            ImagerProfile(user=kwargs.get('instance')).save()
        except (KeyError, ValueError):
            msg = "Unable to create ImagerProfile or {}"
            # logger.error(msg.format(kwargs['instance']))
@receiver(pre_delete, sender=User)
def delete_profile(sender, **kwargs):
    profile = ImagerProfile.objects.get(user=kwargs.get('instance'))
    profile.delete()
