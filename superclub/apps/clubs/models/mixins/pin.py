# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# TODO 일간, 주간, 월간 카운트 로직 구현
# Class Section
class ClubPinModelMixin(models.Model):
    pin_count = models.IntegerField(_('핀 수'), default=0)
    daily_pin_count = models.IntegerField(_('일간 핀 수'), default=0)
    weekly_pin_count = models.IntegerField(_('주간 핀 수'), default=0)
    monthly_pin_count = models.IntegerField(_('월간 핀 수'), default=0)

    class Meta:
        abstract = True

    def update_club_pin_count(self):
        self.pin_count = self.club_pins.filter(is_active=True).count()
