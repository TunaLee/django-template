# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileStaffPermissionMixin(models.Model):
    # Staff Manager Permission
    club_staff_permission = models.BooleanField(_('스태프 임명/취소 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_staff_permission = self.club.staff_permission <= self.permission_grade

        return super(ProfileStaffPermissionMixin, self).save(*args, **kwargs)
