# Django
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Local
from superclub.modules.choices import STAFF_TYPE_CHOICES


class ClubMemberPermissionMixin(models.Model):
    # Member Manager Permission
    auto_member_registration_permission = models.IntegerField(_('자동 가입 권한'), choices=STAFF_TYPE_CHOICES,
                                                           default=9)
    approval_member_permission = models.IntegerField(_('가입 승인 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    restriction_activity_permission = models.IntegerField(_('활동 제한 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    restriction_activity_period_permission = models.IntegerField(_('활동 제한 기간 설정 권한'), choices=STAFF_TYPE_CHOICES,
                                                              default=9)
    banishment_permission = models.IntegerField(_('퇴출 권한'), choices=STAFF_TYPE_CHOICES, default=7)
    restriction_approval_member_period_permission = models.IntegerField(_('가입 제한 기간 설정 꿘한'), choices=STAFF_TYPE_CHOICES,
                                                                    default=9)
    block_permission = models.IntegerField(_('차단 권한'), choices=STAFF_TYPE_CHOICES, default=9)

    __auto_member_registration_permission = None
    __approval_member_permission = None
    __restriction_activity_permission = None
    __restriction_activity_period_permission = None
    __banishment_permission = None
    __restriction_approval_member_period_permission = None
    __block_permission = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__auto_member_registration_permission = self.auto_member_registration_permission
        self.__approval_member_permission = self.approval_member_permission
        self.__restriction_activity_permission = self.restriction_activity_permission
        self.__restriction_activity_period_permission = self.restriction_activity_period_permission
        self.__banishment_permission = self.banishment_permission
        self.__restriction_approval_member_period_permission = self.restriction_approval_member_period_permission
        self.__block_permission = self.block_permission

    def save(self, *args, **kwargs):
        # Check auto_member_registration_permission changed
        if self.auto_member_registration_permission != self.__auto_member_registration_permission:
            # Set auto_member_registration_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.auto_member_registration_permission) & Q(club_auto_member_registration_permission=True)) \
                .update(club_auto_member_registration_permission=False)

            # Set auto_member_registration_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.auto_member_registration_permission) & Q(club_auto_member_registration_permission=False)) \
                .update(club_auto_member_registration_permission=True)

        # Check approval_member_permission changed
        if self.approval_member_permission != self.__approval_member_permission:
            # Set approval_member_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.approval_member_permission) & Q(club_approval_member_permission=True)) \
                .update(club_approval_member_permission=False)

            # Set approval_member_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.approval_member_permission) & Q(club_approval_member_permission=False)) \
                .update(club_approval_member_permission=True)

        # Check restriction_activity_permission changed
        if self.restriction_activity_permission != self.__restriction_activity_permission:
            # Set restriction_activity_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.restriction_activity_permission) & Q(club_restriction_activity_permission=True)) \
                .update(club_restriction_activity_permission=False)

            # Set restriction_activity_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.restriction_activity_permission) & Q(club_restriction_activity_permission=False)) \
                .update(club_restriction_activity_permission=True)

        # Check restriction_activity_period_permission changed
        if self.restriction_activity_period_permission != self.__restriction_activity_period_permission:
            # Set restriction_activity_period_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.restriction_activity_period_permission) & Q(club_restriction_activity_period_permission=True)) \
                .update(club_restriction_activity_period_permission=False)

            # Set restriction_activity_period_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.restriction_activity_period_permission) & Q(
                    club_restriction_activity_period_permission=False)) \
                .update(club_restriction_activity_period_permission=True)

        # Check banishment_permission changed
        if self.banishment_permission != self.__banishment_permission:
            # Set banishment_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.banishment_permission) & Q(
                    club_banishment_permission=True)) \
                .update(club_banishment_permission=False)

            # Set banishment_permission True
            self.profiles \
                .filter(
                Q(staff__gte=self.banishment_permission) & Q(
                    club_banishment_permission=False)) \
                .update(club_banishment_permission=True)

        # Check restriction_approval_member_period_permission changed
        if self.restriction_approval_member_period_permission != self.__restriction_approval_member_period_permission:
            # Set restriction_approval_member_period_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.restriction_approval_member_period_permission) & Q(
                    club_restriction_approval_member_period_permission=True)) \
                .update(club_restriction_approval_member_period_permission=False)

            # Set restriction_approval_member_period_permission True
            self.restriction_approval_member_period_permission \
                .filter(
                Q(staff__gte=self.restriction_approval_member_period_permission) & Q(
                    club_restriction_approval_member_period_permission=False)) \
                .update(club_restriction_approval_member_period_permission=True)

        # Check block_permission changed
        if self.block_permission != self.__block_permission:
            # Set block_permission False
            self.profiles \
                .filter(
                Q(staff__lt=self.block_permission) & Q(
                    club_block_permission=True)) \
                .update(club_block_permission=False)

            # Set block_permission True
            self.block_permission \
                .filter(
                Q(staff__gte=self.block_permission) & Q(
                    club_block_permission=False)) \
                .update(club_block_permission=True)

        return super(ClubMemberPermissionMixin, self).save(*args, **kwargs)
