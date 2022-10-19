# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubStaffPermissionPermissionMixin(models.Model):
    # Permission Manager Permission
    modify_permission_by_staff_permission = models.IntegerField(_('스탭별 권한 수정 권한'), choices=STAFF_TYPE_CHOICES, default=9)
    __modify_permission_by_staff_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__modify_permission_by_staff_permission = self.modify_permission_by_staff_permission

    def save(self, *args, **kwargs):
        # Check modify_permission_by_staff_permission changed
        if self.modify_permission_by_staff_permission != self.__modify_permission_by_staff_permission:
            # Set modify_permission_by_staff_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.modify_permission_by_staff_permission) & Q(club_modify_permission_by_staff_permission=True)) \
                .update(club_modify_permission_by_staff_permission=False)

            # Set modify_permission_by_staff_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.modify_permission_by_staff_permission) & Q(club_modify_permission_by_staff_permission=False)) \
                .update(club_modify_permission_by_staff_permission=True)

        return super(ClubStaffPermissionPermissionMixin, self).save(*args, **kwargs)
