# Django
from django.utils.translation import gettext_lazy as _
from django.db.models import F

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from superclub.apps.boards.api.serializers.update import BoardGroupOrderUpdateSerializer
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer

# Utils
from superclub.utils.api.response import Response
from superclub.utils.exception_handlers import CustomForbiddenException

# Decorators
from superclub.apps.boards.decorators import board_group_order_decorator

# Models
from superclub.apps.boards.models import BoardGroup


# Class Section
class BoardGroupOrderViewMixin:
    @swagger_auto_schema(**board_group_order_decorator(title='5. 게시판 그룹 - Admin', request_body=BoardGroupOrderUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='order', url_name='board_group_order')
    def board_group_order(self, request, pk=None):
        board_group = self.get_object()
        board_group_order = board_group.order
        request_order = request.data['order']
        if board_group.club.user == request.user:
            board_groups = BoardGroup.objects.filter(club=board_group.club.pk)
            if board_group_order > request_order:
                board_groups.filter(order__gte=request_order,
                                    order__lte=board_group_order).update(order=F('order') + 1)
            if board_group_order < request_order:
                board_groups.filter(order__gte=board_group_order,
                                    order__lte=request_order).update(order=F('order') - 1)
            board_group.order = request_order
            board_group.save()
            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message=_('ok'),
                data=BoardGroupListSerializer(instance=board_group).data
            )
        raise CustomForbiddenException('게시판 수정 권한이 없습니다.')
