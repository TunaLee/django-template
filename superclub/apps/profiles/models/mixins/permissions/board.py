# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileBoardPermissionMixin(models.Model):
    # Board Manger Permission
    club_board_permission = models.BooleanField(_('게시판 생성/활성/비활성화 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_board_permission = self.club.board_permission <= self.permission_grade

        return super(ProfileBoardPermissionMixin, self).save(*args, **kwargs)
