# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubDesignPermissionMixin(models.Model):
    # Design Manager Permission
    design_permission = models.IntegerField(_('클럽 디자인 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    __design_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__design_permission = self.design_permission

    def save(self, *args, **kwargs):
        # Check design_permission changed
        if self.design_permission != self.__design_permission:
            # Set design_permission False
            self.profiles \
                .filter(Q(staff__lt=self.design_permission) & Q(club_design_permission=True)) \
                .update(club_design_permission=False)

            # Set design_permission True
            self.profiles \
                .filter(Q(staff__gte=self.design_permission) & Q(club_design_permission=False)) \
                .update(club_design_permission=True)

        return super(ClubDesignPermissionMixin, self).save(*args, **kwargs)
