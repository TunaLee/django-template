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
from superclub.apps.likes.decorators import comment_like_decorator, comment_unlike_decorator, \
    comment_dislike_decorator, comment_undislike_decorator

# Serializers
from superclub.apps.likes.api.serializers.list import CommentLikeListSerializer
from superclub.utils.exception_handlers import CustomBadRequestError


# Class Section
class CommentLikeViewMixin:
    @swagger_auto_schema(**comment_like_decorator(title='9. 댓글 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='like', url_name='comment_like')
    def comment_like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        club = comment.club
        profile = club.profiles.filter(user=user).first()
        instance = user.like_comment(comment, profile)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=CommentLikeListSerializer(instance=instance).data
        )

    # 좋아요 취소
    @swagger_auto_schema(**comment_unlike_decorator(title='9. 댓글 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='unlike', url_name='post_unlike')
    def comment_unlike(self, request, pk=None):
        comment = self.get_object()
        instance = comment.comment_likes.filter(user=request.user).first()
        if not instance:
            raise CustomBadRequestError('좋아요 객체가 없습니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
        )

    @swagger_auto_schema(**comment_dislike_decorator(title='9. 댓글 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='dislike', url_name='comment_dislike')
    def comment_dislike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        club = comment.club
        profile = club.profiles.filter(user=user).first()
        user.dislike_comment(comment, profile)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
        )

    # 싫어요 취소
    @swagger_auto_schema(**comment_undislike_decorator(title='9. 댓글 - Member', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='undislike', url_name='comment_undislike')
    def comment_undislike(self, request, pk=None):
        comment = self.get_object()
        instance = comment.comment_dislikes.filter(user=request.user).first()
        if not instance:
            raise CustomBadRequestError('싫어요 객체가 없습니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
        )
