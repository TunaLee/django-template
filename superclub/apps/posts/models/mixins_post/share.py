# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class PostShareModelMixin(models.Model):
    share_count = models.IntegerField(_('공유 수'), default=0)

    class Meta:
        abstract = True
