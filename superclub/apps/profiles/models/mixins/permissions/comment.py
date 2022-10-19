# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ProfileCommentPermissionMixin(models.Model):
    # Comment Manager Permission
    club_comment_permission = models.BooleanField(_('댓글 활성/비활성화 권한'), null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.club_comment_permission = self.club.comment_permission <= self.permission_grade

        return super(ProfileCommentPermissionMixin, self).save(*args, **kwargs)
