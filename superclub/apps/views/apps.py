from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ViewsConfig(AppConfig):
    name = "superclub.apps.views"
    verbose_name = _('조회수 관리')
