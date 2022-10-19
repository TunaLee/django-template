from rest_framework.permissions import BasePermission

from superclub.apps.profiles.models import Profile


class ClubPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(club_id=obj.id, user=request.user)

        if view.action in ['create', 'partial_update',
                           'me',
                           'club_pin', 'club_unpin', 'club_join', 'club_leave', 'club_share', 'club_tag']:
            return bool(request.user and request.user.is_authenticated)

        # Todo Board group permission 정책 아직 안 나옴 임시
        elif view.action in ['club_board_group']:  # Board group 생성 권한
            return profile.club_board_permission

        elif view.action in ['club_banner_image', 'club_profile_image']:  # 클럽 디자인 권한
            return profile.clubDesignPermission
