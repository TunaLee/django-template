# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProfileCommentModelMixin(models.Model):
    comment_count = models.IntegerField(_('댓글 수'), default=0)

    class Meta:
        abstract = True
