# Django
from django.db.models import F
from django.db.models.aggregates import Max
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework.decorators import action
from rest_framework import status

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response
from superclub.utils.exception_handlers import CustomForbiddenException

# Decorators
from superclub.apps.boards.decorators import board_group_merge_decorator

# Serializers
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer
from superclub.apps.boards.api.serializers.update import BoardGroupMergeUpdateSerializer

# Models
from superclub.apps.boards.models import BoardGroup


# TODO Protect 이슈 해결하기
# Class Section
class BoardGroupMergeViewMixin:
    @swagger_auto_schema(**board_group_merge_decorator(title='5. 게시판 그룹 - Admin', request_body=BoardGroupMergeUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='merge', url_name='board_group_merge')
    def board_group_merge(self, request, pk=None):
        board_group = self.get_object()

        request_board_group = BoardGroup.objects.get(id=request.data['id'])
        max_board = request_board_group.boards.aggregate(order=Max('order'))
        max_board_order = max_board['order']

        if not max_board_order:
            max_board_order = 0
        board_group.boards.update(board_group=request_board_group, order=F('order') + max_board_order)
        board_group.delete()

        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=BoardGroupListSerializer(instance=request_board_group).data
        )
