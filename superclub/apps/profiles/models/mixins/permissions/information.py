# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileInformationPermissionMixin(models.Model):
    # Information Manager Permission
    club_modifying_permission = models.BooleanField(_('정보 수정 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_modifying_permission = self.club.modifying_permission <= self.permission_grade

        return super(ProfileInformationPermissionMixin, self).save(*args, **kwargs)
