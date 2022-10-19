from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TagsConfig(AppConfig):
    name = "superclub.apps.tags"
    verbose_name = _('태그 관리')
