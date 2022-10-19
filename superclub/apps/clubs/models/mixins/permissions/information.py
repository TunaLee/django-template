# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubInformationPermissionMixin(models.Model):
    # Information Manager Permission
    modifying_permission = models.IntegerField(_('정보 수정 권한'), choices=STAFF_TYPE_CHOICES, default=9)
    __modifying_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__modifying_permission = self.modifying_permission

    def save(self, *args, **kwargs):
        # Check board_permission changed
        if self.modifying_permission != self.__modifying_permission:
            # Set BoardPermission False
            self.profiles\
                .filter(Q(staff__lt=self.modifying_permission) & Q(club_modifying_permission=True))\
                .update(club_modifying_permission=False)

            # Set BoardPermission True
            self.profiles\
                .filter(Q(staff__gte=self.modifying_permission) & Q(club_modifying_permission=False))\
                .update(club_modifying_permission=True)

        return super(ClubInformationPermissionMixin, self).save(*args, **kwargs)
