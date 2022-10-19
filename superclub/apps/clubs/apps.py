from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClubsConfig(AppConfig):
    name = "superclub.apps.clubs"
    verbose_name = _('클럽 관리')

    def ready(self):
        import superclub.apps.clubs.signals
