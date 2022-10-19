# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from superclub.apps.comments.api.serilalizers.list import CommentListSerializer
from superclub.apps.comments.api.serilalizers.create import CommentCreateSerializer

# Decorators
from superclub.apps.comments.decorators import post_comment_create_decorator

# Utils
from superclub.utils.api.response import Response

# Models
from superclub.apps.comments.models.index import Comment


# Class Section
class PostCommentViewMixin:
    @swagger_auto_schema(**post_comment_create_decorator(title='7. 게시판 - Member', request_body=CommentCreateSerializer))
    @action(detail=True, methods=['post'], url_path='comment', url_name='post_comment')
    def post_comment(self, request, pk=None):
        user = request.user
        post = self.get_object()
        parent_comment_pk = request.data.pop('parent_comment', None)
        parent_comment = Comment.objects.filter(id=parent_comment_pk).first()
        profile = post.club.profiles.filter(user=user).first()
        instance = Comment.objects.create(parent_comment=parent_comment, club=post.club, user=user,
                                          profile=profile, post=post, **request.data)

        # 자식 댓글 생성 시, 부모 댓글 업데이트
        if parent_comment:
            parent_comment.child_comment_data = [parent_comment.child_comment_data, CommentListSerializer(instance=instance).data]
            parent_comment.save()

        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=CommentListSerializer(instance=instance).data
        )
