# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubPostPermissionMixin(models.Model):
    # Post Manager Permission
    post_permission = models.IntegerField(_('게시글 활성/비활성화 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    __post_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__post_permission = self.post_permission

    def save(self, *args, **kwargs):
        # Check post_permission changed
        if self.post_permission != self.__post_permission:
            # Set post_permission False
            self.profiles\
                .filter(Q(staff__lt=self.post_permission) & Q(club_post_permission=True))\
                .update(club_post_permission=False)

            # Set post_permission True
            self.profiles\
                .filter(Q(staff__gte=self.post_permission) & Q(club_post_permission=False))\
                .update(club_post_permission=True)

        return super(ClubPostPermissionMixin, self).save(*args, **kwargs)
