from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LikesConfig(AppConfig):
    name = "superclub.apps.likes"
    verbose_name = _('좋아요 관리')

    def ready(self):
        import superclub.apps.likes.signals
