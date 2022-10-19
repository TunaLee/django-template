# Django Rest Framework
from rest_framework.permissions import BasePermission

# Local
from superclub.apps.profiles.models import Profile


class PostAdminPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(club_id=obj.club.id, user=request.user)

        if view.action in ['post_activate', 'post_deactivate', 'posts_activate', 'posts_deactivate']:  # Post 활성화/비활성화 권한
            return profile.club_post_permission
