# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model


class Translation(Model):
    ko = models.TextField(_('한국어'), null=True, blank=True)
    en = models.TextField(_('영어'), null=True, blank=True)
    ja = models.TextField(_('일본어'), null=True, blank=True)
    zh = models.TextField(_('중국어'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('번역')
        db_table = 'translations'
        ordering = ['-created']
