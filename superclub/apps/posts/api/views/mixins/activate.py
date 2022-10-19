# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Utils
from superclub.utils.api.response import Response

# Serializer
from superclub.apps.posts.api.serializers.update import PostActiveSerializer, PostsActiveSerializer
from superclub.apps.posts.decorators import post_activate_decorator, post_deactivate_decorator, \
    posts_activate_decorator, posts_deactivate_decorator

# Models
from superclub.apps.posts.models import Post


# Class Section
class PostActivateViewMixin:
    @swagger_auto_schema(**post_activate_decorator(title='7. 게시판 - Admin', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='activate', url_name='post_activate')
    def post_activate(self, request, pk=None):
        post = self.get_object()
        post.is_active = True
        post.save()
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=PostActiveSerializer(instance=post).data
        )


class PostsActivateViewMixin:
    @swagger_auto_schema(**posts_activate_decorator(title='7. 게시판 - Admin', request_body=PostsActiveSerializer))
    @action(detail=False, methods=['post'], url_path='activate', url_name='posts_activate')
    def posts_activate(self, request, pk=None):
        ids = request.data.get('id', None)
        if ids:
            for id in ids:
                post = Post.objects.get(id=id)
                post.is_active = True
                post.save()
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
        )


class PostDeactivateViewMixin:
    @swagger_auto_schema(**post_deactivate_decorator(title='7. 게시판 - Admin', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='deactivate', url_name='post_deactivate')
    def post_deactivate(self, request, pk=None):
        post = self.get_object()
        post.is_active = False
        post.save()
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok')
        )


class PostsDeactivateViewMixin:
    @swagger_auto_schema(**posts_deactivate_decorator(title='7. 게시판 - Admin', request_body=PostsActiveSerializer))
    @action(detail=False, methods=['post'], url_path='deactivate', url_name='posts_deactivate')
    def posts_deactivate(self, request, pk=None):
        ids = request.data.get('id', None)
        if ids:
            for id in ids:
                post = Post.objects.get(id=id)
                post.is_active = False
                post.save()
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
        )
