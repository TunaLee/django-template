from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PinsConfig(AppConfig):
    name = "superclub.apps.pins"
    verbose_name = _('핀 관리')
