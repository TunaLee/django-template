# Manager
from superclub.apps.posts.models.managers.objects import PostMainManager


# Class Section
class PostActiveManager(PostMainManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
