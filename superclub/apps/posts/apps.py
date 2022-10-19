from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostsConfig(AppConfig):
    name = "superclub.apps.posts"
    verbose_name = _('포스트 관리')

    def ready(self):
        import superclub.apps.posts.signals
