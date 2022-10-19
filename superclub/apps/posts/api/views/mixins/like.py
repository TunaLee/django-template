# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.likes.decorators import post_like_decorator, post_unlike_decorator, post_dislike_decorator, \
    post_undislike_decorator

# Serializers
from superclub.apps.likes.api.serializers.list import PostLikeListSerializer
from superclub.utils.exception_handlers import CustomBadRequestError


# Class Section
class PostLikeViewMixin:
    @swagger_auto_schema(**post_like_decorator(title='7. 게시판 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='like', url_name='post_like')
    def post_like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        club = post.club
        profile = club.profiles.filter(user=user).first()
        instance = user.like_post(post, profile)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=PostLikeListSerializer(instance=instance).data
        )

    # 좋아요 취소
    @swagger_auto_schema(**post_unlike_decorator(title='7. 게시판 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='unlike', url_name='post_unlike')
    def post_unlike(self, request, pk=None):
        post = self.get_object()
        instance = post.post_likes.filter(user=request.user).first()
        if not instance:
            raise CustomBadRequestError('좋아요 객체가 없습니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
        )

    @swagger_auto_schema(**post_dislike_decorator(title='7. 게시판 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='dislike', url_name='post_dislike')
    def post_dislike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        club = post.club
        profile = club.profiles.filter(user=user).first()
        user.dislike_post(post, profile)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
        )

    # 싫어요 취소
    @swagger_auto_schema(**post_undislike_decorator(title='7. 게시판 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='undislike', url_name='post_undislike')
    def post_undislike(self, request, pk=None):
        post = self.get_object()
        instance = post.post_dislikes.filter(user=request.user).first()
        if not instance:
            raise CustomBadRequestError('싫어요 객체가 없습니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
        )
