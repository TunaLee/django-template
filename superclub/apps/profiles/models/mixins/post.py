# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProfilePostModelMixin(models.Model):
    post_count = models.IntegerField(_('게시글 수'), default=0)

    class Meta:
        abstract = True

    # TODO 로직 구현하기
    # def update_profile_post_count(self):
