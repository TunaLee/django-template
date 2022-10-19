from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TranslationsConfig(AppConfig):
    name = "superclub.apps.translations"
    verbose_name = _('번역 관리')
