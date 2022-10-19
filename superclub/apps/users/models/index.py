# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from superclub.apps.users.models.mixins.comment_like import CommentLikeModelMixin
from superclub.apps.users.models.mixins.comment_report import CommentReportModelMixin
# Bases
from superclub.bases.models import Model

# Manager
from superclub.apps.users.models.managers.objects import UserMainManager
from superclub.apps.users.models.managers.active import UserActiveManager

# Fields
from superclub.apps.users.models.fields.phone_number import CustomPhoneNumberField

# Mixins
from superclub.apps.users.models.mixins.comment import CommentModelMixin
from superclub.apps.users.models.mixins.club_share import ClubShareModelMixin
from superclub.apps.users.models.mixins.join import JoinModelMixin
from superclub.apps.users.models.mixins.image import ImageModelMixin
from superclub.apps.users.models.mixins.post import PostModelMixin
from superclub.apps.users.models.mixins.club_pin import ClubPinModelMixin
from superclub.apps.users.models.mixins.post_share import PostShareModelMixin
from superclub.apps.users.models.mixins.post_like import PostLikeModelMixin
from superclub.apps.users.models.mixins.post_pin import PostPinModelMixin


# Class Section
class User(AbstractUser,
           Model,
           JoinModelMixin,
           ImageModelMixin,
           PostModelMixin,
           ClubShareModelMixin,
           PostShareModelMixin,
           ClubPinModelMixin,
           PostPinModelMixin,
           PostLikeModelMixin,
           CommentModelMixin,
           CommentLikeModelMixin,
           CommentReportModelMixin):
    email = models.EmailField(_('이메일'), unique=True, null=True, blank=True)
    username = models.CharField(_('닉네임'), unique=True, max_length=100, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # TODO: manager 분기처리 및 queryset 관련 로직들 manager 로 이전
    objects = UserMainManager()
    active = UserActiveManager()

    class Meta:
        verbose_name = verbose_name_plural = _('유저')
        db_table = 'users'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        # Update related objects
        self.posts.exclude(user_email=self.email).update(user_email=self.email)

        super(User, self).save(*args, **kwargs)
