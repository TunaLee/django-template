# Python
import os
from time import strftime, gmtime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from han_duck.apps.lectures.models.mixins_lecture.image import LectureImageModelMixin
from han_duck.apps.lectures.models.mixins_lecture_video.view import LectureVideoViewModelMixin
from han_duck.bases.models import Model


class Lecture(Model,
              LectureImageModelMixin):
    name = models.TextField(_('강의 이름'), null=True, blank=True)
    description = models.TextField(_('강의 설명'), null=True, blank=True)
    price = models.DecimalField(_('강의 비용'), null=True, blank=True, decimal_places=2)

    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='lectures')
    language = models.ForeignKey('languages.Language', on_delete=models.SET_NULL, null=True, blank=True, related_name='lectures')

    class Meta:
        verbose_name = verbose_name_plural = _('강의')
        db_table = 'lecture'
        ordering = ['-created']


class LectureVideo(Model,
                   LectureVideoViewModelMixin):
    lecture = models.ForeignKey('Lecture', verbose_name=_('강의'), on_delete=models.CASCADE, related_name='lecture_videos')
    name = models.TextField(_('강의 제목'), null=True, blank=True)
    description = models.TextField(_('강의 설명'), null=True, blank=True)
    video = models.FileField(_('비디오'))
    video_url = models.URLField(_('비디오 URL'), null=True, blank=True)
    thumbnail_image = models.ImageField(_('썸네일 이미지'), null=True, blank=True)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('강의 비디오')
        db_table = 'lecture_videos'
        ordering = ['-created']

    def __str__(self):
        return f'{self.lecture}'


class LectureImage(Model):

    def image_path(instance, filename):
        upload_to = 'Lecture/DetailImage/'
        time = strftime("%Y%m%dT%H%M%S", gmtime())
        ext = filename.split('.')[-1]
        filename = f'{time}.{ext}'
        return os.path.join(upload_to, filename)

    lecture = models.ForeignKey('Lecture', verbose_name=_('강의'), on_delete=models.CASCADE, related_name='lecture_images')
    image = models.ImageField(_('이미지'), upload_to=image_path)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)
    thumbnail_image = models.ImageField(_('썸네일 이미지'), null=True, blank=True)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('강의 이미지')
        db_table = 'lecture_images'
        ordering = ['-created']

    def __str__(self):
        return self.id
