# Django
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from superclub.apps.boards.models.mixins.permissions.board_group_operation import BoardGroupOperationPermissionMixin
# Permission
from superclub.apps.boards.models.mixins.permissions.cr import BoardCRPermissionMixin
from superclub.apps.boards.models.mixins.permissions.board_operation import BoardOperationPermissionMixin

# Local
from superclub.bases.models import Model

# Modules
from superclub.modules.choices import VIEW_MODE_CHOICES, BOARD_TYPE_CHOICES, BOARD_GROUP_TYPE_CHOICES


# Class Section
class BoardGroup(Model,
                 BoardGroupOperationPermissionMixin,
                 ):
    # Club
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='board_groups')
    club_name = models.CharField(_('이름'), max_length=60, null=True, blank=True)
    name = models.CharField(_('이름'), max_length=100)
    order = models.IntegerField(_('순서'), default=0, validators=[MinValueValidator(1)])
    type = models.CharField(_('타입'), choices=BOARD_GROUP_TYPE_CHOICES, max_length=100, default='NORMAL')

    class Meta:
        verbose_name = verbose_name_plural = _('게시판 그룹')
        db_table = 'board_groups'
        ordering = ['order']

    def __str__(self):
        return f'{self.club_name} {self.name}'

    def save(self, *args, **kwargs):
        # Set club_name
        if self.club:
            self.club_name = self.club.name

        super(BoardGroup, self).save(*args, **kwargs)

        # Update related objects
        self.boards.exclude(is_active=self.is_active).update(is_active=self.is_active)  # 게시판 활성화
        self.boards.exclude(board_group_name=self.name).update(board_group_name=self.name)  # 게시판의 보드 그룹 이름


class Board(Model,
            BoardCRPermissionMixin,
            BoardOperationPermissionMixin
            ):
    # Club
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='boards',
                             null=True)
    club_name = models.CharField(_('클럽 이름'), max_length=60, null=True, blank=True)

    # BoardGroup
    board_group = models.ForeignKey('BoardGroup', verbose_name=_('게시판 그룹'), on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='boards')
    board_group_name = models.CharField(_('그룹 이름'), max_length=60, null=True, blank=True)

    # Basic
    name = models.CharField(_('이름'), max_length=20)
    description = models.CharField(_('설명'), max_length=160, null=True, blank=True)
    view_mode = models.CharField(_('뷰 모드'), choices=VIEW_MODE_CHOICES, max_length=100, default='LIST_TYPE')
    type = models.CharField(_('타입'), choices=BOARD_TYPE_CHOICES, max_length=100, default='NORMAL')
    order = models.IntegerField(_('순서'), default=0, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = verbose_name_plural = _('게시판')
        db_table = 'boards'
        ordering = ['order']

    def __str__(self):
        return f'{self.club_name}/{self.board_group_name}/{self.name}'

    def save(self, *args, **kwargs):
        if not self.club and self.board_group.club:
            self.club = self.board_group.club

        # Set club_name
        self.club_name = self.club.name

        # Set board_group_name
        self.board_group_name = self.board_group.name

        # Update related objects
        self.posts.exclude(board_name=self.name).update(board_name=self.name)
        return super(Board, self).save(*args, **kwargs)
