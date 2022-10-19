# Python
from cached_property import cached_property

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Managers
from superclub.apps.profiles.models.managers.active import ProfileActiveManager
from superclub.apps.profiles.models.managers import ProfileMainManager

# Mixins
from superclub.apps.profiles.models.mixins.permissions.board import ProfileBoardPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.comment import ProfileCommentPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.design import ProfileDesignPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.information import ProfileInformationPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.member import ProfileMemberPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.operation import ProfileOperationPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.post import ProfilePostPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.staff import ProfileStaffPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.staff_permission import ProfileStaffPermissionPermissionMixin
from superclub.apps.profiles.models.mixins.permissions.static import ProfileStaticPermissionMixin
from superclub.apps.profiles.models.mixins.comment import ProfileCommentModelMixin
from superclub.apps.profiles.models.mixins.post import ProfilePostModelMixin
from superclub.apps.profiles.models.mixins.visit import ProfileVisitModelMixin

# Modules
from superclub.modules.choices import MEMBER_TYPE_CHOICES, STAFF_TYPE_CHOICES

# Bases
from superclub.bases.models import Model


class Profile(Model,
              ProfileCommentModelMixin,
              ProfilePostModelMixin,
              ProfileVisitModelMixin,
              ProfileBoardPermissionMixin,
              ProfileCommentPermissionMixin,
              ProfileDesignPermissionMixin,
              ProfileInformationPermissionMixin,
              ProfileMemberPermissionMixin,
              ProfileOperationPermissionMixin,
              ProfilePostPermissionMixin,
              ProfileStaffPermissionMixin,
              ProfileStaffPermissionPermissionMixin,
              ProfileStaticPermissionMixin
              ):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='profiles')
    club_name = models.CharField(_('클럽 이름'), max_length=60, null=True, blank=True)
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='profiles')
    user_email = models.CharField(_('유저 이메일'), max_length=60, null=True, blank=True)
    user_data = models.JSONField(_('유저'), null=True, blank=True)
    point = models.IntegerField(_('점수'), default=0)
    level = models.IntegerField(_('레벨'), default=1)
    grade = models.IntegerField(_('등급'), choices=MEMBER_TYPE_CHOICES, default=1)
    grade_name = models.CharField(_('등급 이름'), max_length=100, default='BRONZE')
    staff = models.IntegerField(_('스태프'), choices=STAFF_TYPE_CHOICES, null=True, blank=True)
    staff_name = models.CharField(_('스태프 이름'), max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(_('스태프 여부'), default=False)

    objects = ProfileMainManager()
    active = ProfileActiveManager()

    class Meta:
        verbose_name = verbose_name_plural = _('클럽 프로필')
        db_table = 'profiles'
        unique_together = ('club', 'user')
        ordering = ['-created']

    @cached_property
    def permission_grade(self):
        return self.staff or self.grade

    def save(self, *args, **kwargs):

        # Set infos
        self.club_name = self.club.name  # club_name
        self.user_email = self.user.email  # user_email

        return super(Profile, self).save(*args, **kwargs)
