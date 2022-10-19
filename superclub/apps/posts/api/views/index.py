# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Filters
from superclub.apps.posts.api.views.filters.posts_filter import PostsFilter, PostsAdminFilter

# Permission
from superclub.apps.posts.api.views.permissions.index import PostAdminPermission

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.utils.decorators import list_decorator, retrieve_decorator, token_patch_decorator, \
    token_destroy_decorator
from superclub.apps.posts.decorators import post_temporary_destroy_decorator

# Serializers
from superclub.apps.posts.api.serializers.list import PostListSerializer, PostAdminListSerializer
from superclub.apps.posts.api.serializers.retrieve import PostRetrieveSerializer
from superclub.apps.posts.api.serializers.update import PostUpdateSerializer

# Mixins
from superclub.apps.posts.api.views.mixins.comment import PostCommentViewMixin
from superclub.apps.posts.api.views.mixins.tag import PostTagViewMixin
from superclub.apps.posts.api.views.mixins.pin import PostPinViewMixin
from superclub.apps.posts.api.views.mixins.share import PostShareViewMixin
from superclub.apps.posts.api.views.mixins.like import PostLikeViewMixin
from superclub.apps.posts.api.views.mixins.activate import PostActivateViewMixin, PostDeactivateViewMixin, \
    PostsActivateViewMixin, PostsDeactivateViewMixin

# Models
from superclub.apps.posts.models.index import Post
from superclub.utils.exception_handlers import CustomBadRequestError


# Class Section
class PostViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  PostCommentViewMixin,
                  PostTagViewMixin,
                  PostShareViewMixin,
                  PostPinViewMixin,
                  PostLikeViewMixin,
                  GenericViewSet):
    serializers = {
        'default': PostRetrieveSerializer,
        'partial_update': PostUpdateSerializer,
    }
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Post.active.all()
        return queryset

    @swagger_auto_schema(**retrieve_decorator(title=_('7. 게시판 - Guest'), serializer=PostRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(**token_patch_decorator(title='7. 게시판 - Member'))
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**token_destroy_decorator(title='7. 게시판 - Member'))
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(**post_temporary_destroy_decorator(title='7. 게시판 - Member'))
    @action(methods=['delete'], detail=True, url_path='temporary', url_name='post_temporary')
    def post_temporary(self, request, pk):
        post = self.get_object()
        if not post.is_temporary:
            raise CustomBadRequestError('임시글이 아닙니다.')
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )


class PostsViewSet(mixins.ListModelMixin,
                   GenericViewSet):
    serializers = {
        'default': PostListSerializer,
    }
    queryset = Post.active.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = PostsFilter
    search_fields = ('title', 'content', 'post_tags__name')
    ordering_fields = ('popularity',)

    @swagger_auto_schema(**list_decorator(title=_('7. 게시판 - Guest'), serializer=PostListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class PostAdminViewSet(PostActivateViewMixin,
                       PostDeactivateViewMixin,
                       GenericViewSet):
    serializers = {
        'default': PostRetrieveSerializer,
    }
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (PostAdminPermission,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Post.objects.filter(report_count__gte=1)
        return queryset


class PostsAdminViewSet(mixins.ListModelMixin,
                        PostsActivateViewMixin,
                        PostsDeactivateViewMixin,
                        GenericViewSet):
    serializers = {
        'default': PostAdminListSerializer,
    }
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = PostsAdminFilter
    ordering_fields = ['report_count', 'report_date']
    queryset = Post.objects.filter(report_count__gte=1)
    permission_classes = (PostAdminPermission,)

    @swagger_auto_schema(**list_decorator(title=_('7. 게시판 - Admin'), serializer=PostAdminListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
