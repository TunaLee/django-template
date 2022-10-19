# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.apps.club_counts.models.index import ClubDailyCommentCount
from superclub.apps.comments.models.index import Comment


class ClubCommentModelMixin(models.Model):
    comment_count = models.IntegerField(_('댓글 수'), default=0)
    daily_comment_count = models.IntegerField(_('일간 댓글 수'), default=0)
    weekly_comment_count = models.IntegerField(_('주간 댓글 수'), default=0)
    monthly_comment_count = models.IntegerField(_('월간 댓글 수'), default=0)

    class Meta:
        abstract = True

    def get_daily_comment_count(self):
        club_daily_comment_counts = self.club_daily_comment_counts.filter(date=datetime.date.today())
        if club_daily_comment_counts:
            return club_daily_comment_counts.count
        return 0

    def update_comment_count(self):
        self.comment_count = Comment.objects.filter(club=self).count()

    def update_daily_comment_count(self, date=datetime.date.today()):
        club_daily_comment_count, created = ClubDailyCommentCount.objects.get_or_create(club=self, date=date)
        club_daily_comment_count.count = Comment.objects.filter(club=self, created__date33=date).count()
        club_daily_comment_count.save()
