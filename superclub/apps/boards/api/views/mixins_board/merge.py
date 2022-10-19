# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework.decorators import action
from rest_framework import status

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.boards.decorators import board_merge_update_decorator

# Serializers
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer
from superclub.apps.boards.api.serializers.update import BoardMergeUpdateSerializer

# Models
from superclub.apps.boards.models import Board


# Class Section
class BoardMergeViewMixin:
    @swagger_auto_schema(**board_merge_update_decorator(title='6. 게시판 - Admin', request_body=BoardMergeUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='merge', url_name='board_merge')
    def board_merge(self, request, pk=None):
        board = self.get_object()

        request_board = Board.objects.get(id=request.data['id'])

        if board.posts.count() + request_board.posts.count() > 10:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('There are more than 10 posts on both boards.')
            )

        board.posts.update(board=request_board)
        board.delete()

        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=BoardGroupListSerializer(instance=request_board.board_group).data
        )
