# Python
import os
from time import strftime, gmtime

# Django
from django.utils.translation import gettext_lazy as _
from django.db import models


# Function Section
def image_path(path, filename):
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(path, filename)


# TODO: 이미지 override 문제
def thumbnail_image_path(instance, filename):
    return image_path('Club/ThumbnailImage/', filename)


def profile_image_path(instance, filename):
    return image_path('Club/ProfileImage/', filename)


def banner_image_path(instance, filename):
    return image_path('Club/BannerImage/', filename)


# Class Section
class ClubImageModelMixin(models.Model):
    thumbnail_image = models.ImageField(_('썸네일 이미지'), upload_to=thumbnail_image_path, blank=True, null=True)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), blank=True, null=True)
    profile_image = models.ImageField(_('프로필 이미지'), upload_to=profile_image_path, blank=True, null=True)
    profile_image_url = models.URLField(_('프로필 이미지 URL'), blank=True, null=True)
    banner_image = models.ImageField(_('배너 이미지'), upload_to=banner_image_path, blank=True, null=True)
    banner_image_url = models.URLField(_('배너 이미지 URL'), blank=True, null=True)

    class Meta:
        abstract = True
