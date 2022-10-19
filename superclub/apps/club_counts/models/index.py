# Django
import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Local
from superclub.bases.models import Model


class ClubDailyViewCount(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE,
                             related_name='club_daily_view_counts')
    count = models.IntegerField(verbose_name='일별 조회수', default=0)
    date = models.DateField(verbose_name='조회 날짜', default=timezone.now)

    class Meta:
        unique_together = ('club', 'date',)
        verbose_name = verbose_name_plural = "일별 조회"


class ClubDailyPostCount(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE,
                             related_name='club_daily_post_counts')
    count = models.IntegerField(verbose_name='일별 포스트 수', default=0)
    date = models.DateField(verbose_name='포스트 날짜', default=timezone.now)

    class Meta:
        unique_together = ('club', 'date',)
        verbose_name = verbose_name_plural = "일별 포스트"


class ClubDailyMemberCount(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE,
                             related_name='club_daily_member_counts')
    count = models.IntegerField(verbose_name='일별 가입 수', default=0)
    date = models.DateField(verbose_name='가입 날짜', default=timezone.now)

    class Meta:
        unique_together = ('club', 'date',)
        verbose_name = verbose_name_plural = "일별 가입"


class ClubDailyCommentCount(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE,
                             related_name='club_daily_comment_counts')
    count = models.IntegerField(verbose_name='일별 댓글 수', default=0)
    date = models.DateField(verbose_name='댓글 날짜', default=timezone.now)

    class Meta:
        unique_together = ('club', 'date',)
        verbose_name = verbose_name_plural = "일별 댓글"
