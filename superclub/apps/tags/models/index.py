# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Mixins
from superclub.apps.tags.models.mixins.club import TagClubModelMixin
from superclub.apps.tags.models.mixins.post import TagPostModelMixin

# Models
from superclub.bases.models import Model


class Tag(Model,
          TagPostModelMixin,
          TagClubModelMixin):
    name = models.CharField(_('이름'), max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('태그')
        db_table = 'tags'
        ordering = ['-post_count']
