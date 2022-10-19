# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubStaticPermissionMixin(models.Model):
    # Static Manager Permission
    static_permission = models.IntegerField(_('통계 관리 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    __static_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__static_permission = self.static_permission

    def save(self, *args, **kwargs):
        # Check static_permission changed
        if self.static_permission != self.__static_permission:
            # Set static_permission False
            self.profiles \
                .filter(Q(staff__lt=self.static_permission) & Q(club_static_permission=True)) \
                .update(club_static_permission=False)

            # Set staff_permission True
            self.profiles \
                .filter(Q(staff__gte=self.static_permission) & Q(club_static_permission=False)) \
                .update(club_static_permission=True)

        return super(ClubStaticPermissionMixin, self).save(*args, **kwargs)
