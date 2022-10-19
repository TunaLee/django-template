# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileStaticPermissionMixin(models.Model):
    # Static Manager Permission
    club_static_permission = models.BooleanField(_('통계 관리 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_static_permission = self.club.static_permission <= self.permission_grade

        return super(ProfileStaticPermissionMixin, self).save(*args, **kwargs)
