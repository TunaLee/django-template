# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.apps.club_counts.models.index import ClubDailyMemberCount


class ClubMemberModelMixin(models.Model):
    member_count = models.IntegerField(_('멤버 수'), default=0)
    daily_member_count = models.IntegerField(_('일간 멤버 수'), default=0)
    weekly_member_count = models.IntegerField(_('주간 멤버 수'), default=0)
    monthly_member_count = models.IntegerField(_('월간 멤버 수'), default=0)

    class Meta:
        abstract = True

    def get_daily_member_count(self):
        club_daily_member_counts = self.club_daily_member_counts.filter(date=datetime.date.today()).first()
        if club_daily_member_counts:
            return club_daily_member_counts.count
        return 0

    def update_member_count(self):
        self.member_count = self.joins.count()

    def update_daily_member_count(self, date=datetime.date.today()):
        club_daily_member_count, created = ClubDailyMemberCount.objects.get_or_create(club=self, date=date)
        club_daily_member_count.count = self.joins.filter(created__date=date).count()
        club_daily_member_count.save()
