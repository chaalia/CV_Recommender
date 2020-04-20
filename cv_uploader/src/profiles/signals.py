from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import logging
from . import models
from .models import BaseProfile

logger = logging.getLogger("project")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, update_fields, **kwargs):
    # post_save.disconnect(create_profile_handler, sender=BaseProfile)
    # import pdb;pdb.set_trace()
    if created:
        profile = BaseProfile(user=instance)
        setattr(instance.baseprofile, "skip_signal", True)
        profile.save()
        delattr(instance.baseprofile, "skip_signal")
        logger.info("New user profile for {} created".format(instance))
    # Create the profile object, only if it is newly created
    # post_save.connect(create_profile_handler, sender=BaseProfile)
    # if 'document' in update_fields :
    #     import pdb;pdb.set_trace()




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = Profile.objects.create(user=instance)
#         profile.save()

@receiver(post_save, sender=BaseProfile)
def treat_uploaded_cv(sender, instance, created ,update_fields , **kwargs ):
	# import pdb;pdb.set_trace()
	pass