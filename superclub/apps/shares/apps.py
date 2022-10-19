from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SharesConfig(AppConfig):
    name = "superclub.apps.shares"
    verbose_name = _('공유 관리')
