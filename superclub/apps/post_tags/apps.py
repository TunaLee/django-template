from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostTagsConfig(AppConfig):
    name = "superclub.apps.post_tags"
    verbose_name = _('게시글 태그')
