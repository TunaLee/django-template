# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileMemberPermissionMixin(models.Model):
    # Member Manager Permission
    club_auto_member_registration_permission = models.BooleanField(_('자동 가입 권한'), null=True, blank=True)
    club_approval_member_permission = models.BooleanField(_('가입 승인 권한'), null=True, blank=True)
    club_restriction_activity_permission = models.BooleanField(_('활동 제한 권한'), null=True, blank=True)
    club_restriction_activity_period_permission = models.BooleanField(_('활동 제한 기간 설정 권한'), null=True, blank=True)
    club_banishment_permission = models.BooleanField(_('퇴출 권한'), null=True, blank=True)
    club_restriction_approval_member_period_permission = models.BooleanField(_('가입 제한 기간 설정 꿘한'), null=True, blank=True)
    club_block_permission = models.BooleanField(_('차단 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_auto_member_registration_permission = self.club.auto_member_registration_permission <= self.permission_grade
        self.club_approval_member_permission = self.club.approval_member_permission <= self.permission_grade
        self.club_restriction_activity_permission = self.club.restriction_activity_permission <= self.permission_grade
        self.club_restriction_activity_period_permission = self.club.restriction_activity_period_permission <= self.permission_grade
        self.club_banishment_permission = self.club.banishment_permission <= self.permission_grade
        self.club_restriction_approval_member_period_permission = self.club.restriction_approval_member_period_permission <= self.permission_grade
        self.club_block_permission = self.club.block_permission <= self.permission_grade

        return super(ProfileMemberPermissionMixin, self).save(*args, **kwargs)
