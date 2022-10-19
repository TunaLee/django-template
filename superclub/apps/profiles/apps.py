from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfilesConfig(AppConfig):
    name = "superclub.apps.profiles"
    verbose_name = _('프로필')
