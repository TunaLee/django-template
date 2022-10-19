# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileOperationPermissionMixin(models.Model):
    # Operation Manager Permission
    club_hand_over_permission = models.BooleanField(_('양도 권한'), null=True, blank=True)
    club_transfer_permission = models.BooleanField(_('이전 권한'), null=True, blank=True)
    club_independence_permission = models.BooleanField(_('독립 권한'), null=True, blank=True)
    club_merge_permission = models.BooleanField(_('합병 권한'), null=True, blank=True)
    club_closure_permission = models.BooleanField(_('폐쇄 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_hand_over_permission = self.club.hand_over_permission <= self.permission_grade
        self.club_transfer_permission = self.club.transfer_permission <= self.permission_grade
        self.club_independence_permission = self.club.independence_permission <= self.permission_grade
        self.club_merge_permission = self.club.merge_permission <= self.permission_grade
        self.club_closure_permission = self.club.closure_permission <= self.permission_grade

        return super(ProfileOperationPermissionMixin, self).save(*args, **kwargs)
