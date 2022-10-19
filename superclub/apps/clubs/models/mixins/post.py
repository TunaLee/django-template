# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.apps.club_counts.models.index import ClubDailyPostCount
from superclub.apps.posts.models.index import Post


class ClubPostModelMixin(models.Model):
    post_count = models.IntegerField(_('게시글 수'), default=0)
    daily_post_count = models.IntegerField(_('일간 게시글 수'), default=0)
    weekly_post_count = models.IntegerField(_('주간 게시글 수'), default=0)
    monthly_post_count = models.IntegerField(_('월간 게시글 수'), default=0)

    class Meta:
        abstract = True

    def get_daily_post_count(self):
        club_daily_post_counts = self.club_daily_post_counts.filter(date=datetime.date.today()).first()
        if club_daily_post_counts:
            return club_daily_post_counts.count
        return 0

    def update_post_count(self):
        self.post_count = Post.objects.filter(club=self).count()

    def update_daily_post_count(self, date=datetime.date.today()):
        club_daily_post_count, created = ClubDailyPostCount.objects.get_or_create(club=self, date=date)
        club_daily_post_count.count = Post.objects.filter(club=self, created__date=date).count()
        club_daily_post_count.save()
