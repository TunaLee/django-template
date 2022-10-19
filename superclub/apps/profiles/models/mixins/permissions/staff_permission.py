# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileStaffPermissionPermissionMixin(models.Model):
    # Permission Manager Permission
    club_modify_permission_by_staff_permission = models.BooleanField(_('스탭별 권한 수정 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_modify_permission_by_staff_permission = self.club.modify_permission_by_staff_permission <= self.permission_grade

        return super(ProfileStaffPermissionPermissionMixin, self).save(*args, **kwargs)
