from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from .utils import preprocess_pdf


class BaseProfile(models.Model):

    __original_document = None
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField(
        "Profile picture", upload_to="profile_pics/%Y-%m-%d/", null=True, blank=True
    )
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    document = models.FileField(upload_to='CVS//%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self ,*args ,**kwargs ):
        try :
            old_profile = BaseProfile.objects.get(pk=self.pk)
            current_profile = self
            if self.document is not None or old_profile.document != self.document :
            # import pdb;pdb.set_trace()
                pass
            if old_profile.document != self.document :
                self.__original_document = old_profile.document
                # import pdb;pdb.set_trace()
                preprocess_pdf(self.document.path,self.document)
        except :
            pass
        
        
        super(BaseProfile ,self).save(*args ,**kwargs)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return "{}'s profile".format(self.user)


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile".format(self.user)
