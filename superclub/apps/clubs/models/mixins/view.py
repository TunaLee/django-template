# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.apps.club_counts.models.index import ClubDailyViewCount
from superclub.apps.views.models.index import ClubView


class ClubViewModelMixin(models.Model):
    view_count = models.IntegerField(_('조회수'), default=0)
    daily_view_count = models.IntegerField(_('일간 조회수'), default=0)
    weekly_view_count = models.IntegerField(_('주간 조회수'), default=0)
    monthly_view_count = models.IntegerField(_('월간 조회수'), default=0)

    class Meta:
        abstract = True

    def get_daily_view_count(self):
        club_daily_view_counts = self.club_daily_view_counts.filter(date=datetime.date.today()).first()
        if club_daily_view_counts:
            return club_daily_view_counts.count
        return 0

    def update_view_count(self):
        self.view_count = ClubView.objects.filter(club=self).count()

    def update_daily_view_count(self, date=datetime.date.today()):
        club_daily_view_count, created = ClubDailyViewCount.objects.get_or_create(club=self, date=date)
        club_daily_view_count.count = ClubView.objects.filter(club=self, date__date=date).count()
        club_daily_view_count.save()
