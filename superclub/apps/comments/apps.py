from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommentsConfig(AppConfig):
    name = "superclub.apps.comments"
    verbose_name = _('댓글 관리')

    def ready(self):
        import superclub.apps.comments.signals
