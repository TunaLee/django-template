# Manager
from superclub.apps.profiles.models.managers import ProfileMainManager


# Class Section
class ProfileActiveManager(ProfileMainManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
