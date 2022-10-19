# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Choices
from superclub.modules.choices import USER_TYPE_CHOICES


class BoardCRPermissionMixin(models.Model):
    # CR Manager Permission
    write_permission = models.IntegerField(_('게시글 작성 권한'), choices=USER_TYPE_CHOICES, default=1)
    read_permission = models.IntegerField(_('게시글 조회 권한'), choices=USER_TYPE_CHOICES, default=0)

    class Meta:
        abstract = True
