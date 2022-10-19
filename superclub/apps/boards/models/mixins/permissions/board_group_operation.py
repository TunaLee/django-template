# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Choices
from superclub.modules.choices import STAFF_TYPE_CHOICES


class BoardGroupOperationPermissionMixin(models.Model):
    # Operation Manager Permission
    merge_permission = models.IntegerField(_('게시판 그룹 합병'), choices=STAFF_TYPE_CHOICES, default=7)

    class Meta:
        abstract = True
