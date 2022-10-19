# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.boards.decorators import club_board_group_create_decorator

# Serializers
from superclub.apps.boards.api.serializers.create import BoardGroupCreateSerializer
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer


# Class Section
class ClubBoardGroupViewMixin:
    @swagger_auto_schema(**club_board_group_create_decorator(title='4. 클럽 - Admin', request_body=BoardGroupCreateSerializer))
    @action(detail=True, methods=['post'], url_path='board-group', url_name='club_board_group')
    def club_board_group(self, request, pk=None):
        club = self.get_object()
        name = request.data['name']
        is_active = request.data['is_active']
        instance = club.board_group_club(name, is_active)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=BoardGroupListSerializer(instance=instance).data
        )
