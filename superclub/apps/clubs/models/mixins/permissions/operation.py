# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubOperationPermissionMixin(models.Model):
    # Operation Manager Permission
    hand_over_permission = models.IntegerField(_('양도 권한'), choices=STAFF_TYPE_CHOICES, default=10)
    transfer_permission = models.IntegerField(_('이전 권한'), choices=STAFF_TYPE_CHOICES, default=10)
    independence_permission = models.IntegerField(_('독립 권한'), choices=STAFF_TYPE_CHOICES, default=10)
    merge_permission = models.IntegerField(_('합병 권한'), choices=STAFF_TYPE_CHOICES, default=10)
    closure_permission = models.IntegerField(_('폐쇄 권한'), choices=STAFF_TYPE_CHOICES, default=10)

    __hand_over_permission = None
    __transfer_permission = None
    __independence_permission = None
    __merge_permission = None
    __closure_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hand_over_permission = self.hand_over_permission
        self.__transfer_permission = self.transfer_permission
        self.__independence_permission = self.independence_permission
        self.__merge_permission = self.merge_permission
        self.__closure_permission = self.closure_permission

    def save(self, *args, **kwargs):
        # Check hand_over_permission changed
        if self.hand_over_permission != self.__hand_over_permission:
            # Set hand_over_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.hand_over_permission) & Q(club_hand_over_permission=True)) \
                .update(club_hand_over_permission=False)

            # Set hand_over_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.hand_over_permission) & Q(club_hand_over_permission=False)) \
                .update(club_hand_over_permission=True)

        # Check transfer_permission changed
        if self.transfer_permission != self.__transfer_permission:
            # Set transfer_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.transfer_permission) & Q(club_transfer_permission=True)) \
                .update(club_transfer_permission=False)

            # Set transfer_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.transfer_permission) & Q(club_transfer_permission=False)) \
                .update(club_transfer_permission=True)

        # Check independence_permission changed
        if self.independence_permission != self.__independence_permission:
            # Set independence_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.independence_permission) & Q(club_independence_permission=True)) \
                .update(club_independence_permission=False)

            # Set independence_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.independence_permission) & Q(club_independence_permission=False)) \
                .update(club_independence_permission=True)

        # Check merge_permission changed
        if self.merge_permission != self.__merge_permission:
            # Set merge_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.merge_permission) & Q(club_merge_permission=True)) \
                .update(club_merge_permission=False)

            # Set merge_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.merge_permission) & Q(
                    club_merge_permission=False)) \
                .update(club_merge_permission=True)

        # Check closure_permission changed
        if self.closure_permission != self.__closure_permission:
            # Set closure_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.closure_permission) & Q(
                    club_closure_permission=True)) \
                .update(club_closure_permission=False)

            # Set closure_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.closure_permission) & Q(
                    club_closure_permission=False)) \
                .update(club_closure_permission=True)

        super(ClubOperationPermissionMixin, self).save(*args, **kwargs)
