# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# DRF
from url_filter.validators import MinLengthValidator

# Mixins
from superclub.apps.clubs.models.mixins.board_group import ClubBoardGroupModelMixin
from superclub.apps.clubs.models.mixins.comment import ClubCommentModelMixin
from superclub.apps.clubs.models.mixins.image import ClubImageModelMixin
from superclub.apps.clubs.models.mixins.member import ClubMemberModelMixin
from superclub.apps.clubs.models.mixins.permissions.board import ClubBoardPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.comment import ClubCommentPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.design import ClubDesignPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.information import ClubInformationPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.member import ClubMemberPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.operation import ClubOperationPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.staff_permission import ClubStaffPermissionPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.post import ClubPostPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.staff import ClubStaffPermissionMixin
from superclub.apps.clubs.models.mixins.permissions.static import ClubStaticPermissionMixin
from superclub.apps.clubs.models.mixins.pin import ClubPinModelMixin
from superclub.apps.clubs.models.mixins.post import ClubPostModelMixin
from superclub.apps.clubs.models.mixins.share import ClubShareModelMixin
from superclub.apps.clubs.models.mixins.tag import ClubTagModelMixin
from superclub.apps.clubs.models.mixins.view import ClubViewModelMixin

# Models
from superclub.bases.models import Model


class Club(Model,
           ClubPostModelMixin,
           ClubViewModelMixin,
           ClubMemberModelMixin,
           ClubCommentModelMixin,
           ClubImageModelMixin,
           ClubBoardGroupModelMixin,
           ClubTagModelMixin,
           ClubShareModelMixin,
           ClubPinModelMixin,
           ClubBoardPermissionMixin,
           ClubCommentPermissionMixin,
           ClubDesignPermissionMixin,
           ClubInformationPermissionMixin,
           ClubMemberPermissionMixin,
           ClubOperationPermissionMixin,
           ClubStaffPermissionPermissionMixin,
           ClubPostPermissionMixin,
           ClubStaffPermissionMixin,
           ClubStaticPermissionMixin):
    user = models.ForeignKey('users.User', verbose_name=_('관리자'), on_delete=models.CASCADE, related_name='clubs')
    category = models.ForeignKey('categories.Category', verbose_name=_('카테고리'), on_delete=models.CASCADE,
                                 related_name='clubs')

    user_data = models.JSONField(_('관리자 데이터'), null=True, blank=True)
    name = models.CharField(_('클럽명'), max_length=60, unique=True,
                            validators=[MinLengthValidator(1)],
                            error_messages={'unique': _('Already in use. Please enter a different name.')})
    description = models.CharField(_('설명'), max_length=300, null=True, blank=True)
    address = models.CharField(_('주소'), max_length=20, unique=True,
                               validators=[MinLengthValidator(1)],
                               error_messages={'unique': _('Already in use. Please enter a different address.')})
    board_data = models.JSONField(_('게시판 데이터'), null=True, blank=True)
    popularity = models.IntegerField(_('인기'), default=0)
    is_auto_approval = models.BooleanField(_('자동 승인 여부'), default=True)

    class Meta:
        verbose_name = verbose_name_plural = _('클럽')
        db_table = 'clubs'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(Club, self).save(*args, **kwargs)

        # Update related objects
        self.board_groups.exclude(club_name=self.name).update(club_name=self.name)
        self.boards.exclude(club_name=self.name).update(club_name=self.name)
        self.posts.exclude(club_name=self.name).update(club_name=self.name)
        self.profiles.exclude(club_name=self.name).update(club_name=self.name)

        # Category Club Count
        self.category.update_category_club_count()
        self.category.save()

    def __str__(self):
        return self.name
