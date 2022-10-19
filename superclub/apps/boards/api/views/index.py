# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

# Permissions
from superclub.apps.boards.permission import BoardPermission, BoardGroupPermission

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet
from superclub.utils.api.response import Response

# Utils
from superclub.utils.decorators import token_patch_decorator, retrieve_decorator, destroy_decorator

# Serializers
from superclub.apps.boards.api.serializers.create import BoardGroupCreateSerializer, BoardCreateSerializer
from superclub.apps.boards.api.serializers.retreive import BoardRetrieveSerializer, BoardGroupRetrieveSerializer

# Mixins
from superclub.apps.boards.api.views.mixins_board_group.board import BoardGroupBoardViewMixin
from superclub.apps.boards.api.views.mixins_board_group.order import BoardGroupOrderViewMixin
from superclub.apps.boards.api.views.mixins_board_group.merge import BoardGroupMergeViewMixin
from superclub.apps.boards.api.views.mixins_board.merge import BoardMergeViewMixin
from superclub.apps.boards.api.views.mixins_board.order import BoardOrderViewMixin

# Models
from superclub.apps.boards.models import Board, BoardGroup


# Class Section
class BoardGroupViewSet(mixins.RetrieveModelMixin,
                        GenericViewSet):
    serializers = {
        'default': BoardGroupRetrieveSerializer,
    }
    queryset = BoardGroup.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**retrieve_decorator(title=_('5. 게시판 그룹 - Guest'), serializer=BoardGroupRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)


class BoardViewSet(mixins.RetrieveModelMixin,
                   GenericViewSet):
    serializers = {
        'default': BoardRetrieveSerializer,
    }
    queryset = Board.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**retrieve_decorator(title=_('6. 게시판 - Guest'), serializer=BoardRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)


class BoardGroupAdminViewSet(mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             BoardGroupOrderViewMixin,
                             BoardGroupMergeViewMixin,
                             BoardGroupBoardViewMixin,
                             GenericViewSet):
    serializers = {
        'default': BoardGroupCreateSerializer,
    }
    queryset = BoardGroup.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (BoardGroupPermission,)

    @swagger_auto_schema(**token_patch_decorator(title='5. 게시판 그룹 - Admin'))
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**destroy_decorator(title='5. 게시판 그룹 - Admin'))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.posts.exists():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('Posts must be blank to delete.')
            )
        self.perform_destroy(instance)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )


class BoardAdminViewSet(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        BoardMergeViewMixin,
                        BoardOrderViewMixin,
                        GenericViewSet):
    serializers = {
        'default': BoardCreateSerializer,
    }
    queryset = Board.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (BoardPermission,)

    @swagger_auto_schema(**token_patch_decorator(title='6. 게시판 - Admin'))
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**destroy_decorator(title='6. 게시판 - Admin'))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.posts.exists():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('Posts must be blank to delete.')
            )
        self.perform_destroy(instance)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )
