# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubCommentPermissionMixin(models.Model):
    # Comment Manager Permission
    comment_permission = models.IntegerField(_('댓글 활성/비활성화 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    __comment_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__comment_permission = self.comment_permission

    def save(self, *args, **kwargs):
        if self.comment_permission != self.__comment_permission:
            self.profiles.\
                filter(Q(staff__lt=self.comment_permission) & Q(club_comment_permission=True)).\
                update(club_comment_permission=False)

            self.profiles. \
                filter(Q(staff__gte=self.comment_permission) & Q(club_comment_permission=False)). \
                update(club_comment_permission=True)

        return super(ClubCommentPermissionMixin, self).save(*args, **kwargs)
