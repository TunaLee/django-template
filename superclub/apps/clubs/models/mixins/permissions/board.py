# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubBoardPermissionMixin(models.Model):
    # Board Manger Permission
    board_permission = models.IntegerField(_('게시판 생성/활성/비활성화 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    __board_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__board_permission = self.board_permission

    def save(self, *args, **kwargs):
        # Check board_permission changed
        if self.board_permission != self.__board_permission:
            # Set board_permission False
            self.profiles\
                .filter(Q(staff__lt=self.board_permission) & Q(club_board_permission=True))\
                .update(club_board_permission=False)

            # Set board_permission True
            self.profiles\
                .filter(Q(staff__gte=self.board_permission) & Q(club_board_permission=False))\
                .update(club_board_permission=True)

        return super(ClubBoardPermissionMixin, self).save(*args, **kwargs)
