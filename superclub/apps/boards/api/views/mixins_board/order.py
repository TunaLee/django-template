# Django
from django.db.models import F
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
from superclub.apps.boards.decorators import board_order_update_decorator

# Serializers
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer
from superclub.apps.boards.api.serializers.update import BoardOrderUpdateSerializer

# Models
from superclub.apps.boards.models import Board, BoardGroup


# Class Section
class BoardOrderViewMixin:
    @swagger_auto_schema(**board_order_update_decorator(title='6. 게시판 - Admin', request_body=BoardOrderUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='order', url_name='board_order')
    def board_order(self, request, pk=None):
        board = self.get_object()
        board_order = board.order
        request_order = request.data['order']
        request_board_group = BoardGroup.objects.get(id=request.data['board_group'])

        if board.board_group.club.user == request.user:

            board_groups = Board.objects.filter(board_group__club__pk=board.board_group.club.pk,
                                                board_group=board.board_group)
            request_board_groups = Board.objects.filter(board_group__club__pk=board.board_group.club.pk,
                                                        board_group=request_board_group)

            # 보드 그룹이 같을 때
            if board.board_group == request_board_group:
                if board_order > request_order:
                    board_groups.filter(order__gte=request_order,
                                        order__lte=board_order).update(order=F('order') + 1)
                if board_order < request_order:
                    board_groups.filter(order__gte=board_order,
                                        order__lte=request_order).update(order=F('order') - 1)
            # 보드 그룹이 다를 때
            else:
                board_groups.filter(order__gt=board_order).update(order=F('order') - 1)
                request_board_groups.filter(order__gte=request_order).update(order=F('order') + 1)

            board.order = request_order
            board.board_group = request_board_group
            board.save()

            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message=_('ok'),
                data=BoardGroupListSerializer(instance=board.board_group).data
            )
        raise CustomForbiddenException('게시판 수정 권한이 없습니다.')
