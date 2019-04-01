from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from .appconfig import MB_STORAGE

# Create your models here.


def image_upload_path(instance, filename):
    return "user{0}/image/{1}".format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE)
    phone = models.CharField(_("Phone"), max_length=50)
    address = models.CharField(_("Address"), max_length=150)
    user_image = models.ImageField(
        _("User Photo"), upload_to=image_upload_path, storage=MB_STORAGE)

    def __str__(self):
        return self.user.username
