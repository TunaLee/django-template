# Manager
from superclub.apps.joins.models.managers.objects import JoinMainManager


# Class Section
class JoinActiveManager(JoinMainManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
