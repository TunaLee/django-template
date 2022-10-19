from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    name = "superclub.apps.reports"
    verbose_name = _('신고')

    def ready(self):
        import superclub.apps.reports.signals
