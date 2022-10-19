from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class JoinsConfig(AppConfig):
    name = "superclub.apps.joins"
    verbose_name = _('조인 관리')

    def ready(self):
        import superclub.apps.joins.signals
