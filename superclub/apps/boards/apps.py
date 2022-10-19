from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BoardsConfig(AppConfig):
    name = "superclub.apps.boards"
    verbose_name = _('게시판 관리')

    def ready(self):
        import superclub.apps.boards.signals
