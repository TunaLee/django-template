from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClubCountsConfig(AppConfig):
    name = "superclub.apps.club_counts"
    verbose_name = _('클럽 카운트 관리')
