# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubStaffPermissionMixin(models.Model):
    # Staff Manager Permission
    staff_permission = models.IntegerField(_('스태프 임명/취소 권한'), choices=STAFF_TYPE_CHOICES, default=8)
    __staff_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__staff_permission = self.staff_permission

    def save(self, *args, **kwargs):
        # Check staff_permission changed
        if self.staff_permission != self.__staff_permission:
            # Set staff_permission False
            self.profiles\
                .filter(Q(staff__lt=self.staff_permission) & Q(club_staff_permission=True))\
                .update(club_staff_permission=False)

            # Set staff_permission True
            self.profiles\
                .filter(Q(staff__gte=self.staff_permission) & Q(club_staff_permission=False))\
                .update(club_staff_permission=True)

        return super(ClubStaffPermissionMixin, self).save(*args, **kwargs)
