# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from superclub.apps.boards.api.serializers.create import BoardCreateSerializer
from superclub.apps.boards.api.serializers.retreive import BoardRetrieveSerializer

# Utils
from superclub.utils.api.response import Response
from superclub.utils.exception_handlers import CustomForbiddenException

# Decorators
from superclub.apps.boards.decorators import board_group_board_create_decorator

# Models
from superclub.apps.boards.models import Board


# Class Section
class BoardGroupBoardViewMixin:
    @swagger_auto_schema(**board_group_board_create_decorator(title='5. 게시판 그룹 - Admin', request_body=BoardCreateSerializer))
    @action(detail=True, methods=['post'], url_path='board', url_name='board_group_board')
    def board_group_board(self, request, pk=None):
        board_group = self.get_object()
        instance = Board.objects.create(board_group=board_group, **request.data)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=BoardRetrieveSerializer(instance=instance).data
        )
