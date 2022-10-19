from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "superclub.apps.users"
    verbose_name = _('유저 관리')

    def ready(self):
        try:
            import superclub.apps.users.signals  # noqa F401
        except ImportError:
            pass
