# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfilePostPermissionMixin(models.Model):
    # Post Manager Permission
    club_post_permission = models.BooleanField(_('게시글 활성/비활성화 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_post_permission = self.club.post_permission <= self.permission_grade

        return super(ProfilePostPermissionMixin, self).save(*args, **kwargs)
