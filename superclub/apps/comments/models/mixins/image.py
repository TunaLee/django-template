# Python
import os
from time import strftime, gmtime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Function Section
def image_path(instance, filename):
    upload_to = 'Comment/DetailImage/'
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(upload_to, filename)


# Class Section
class ImageModelMixin(models.Model):
    image = models.ImageField(_('이미지'), upload_to=image_path, null=True, blank=True)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)

    class Meta:
        abstract = True
