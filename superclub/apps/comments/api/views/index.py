# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Decorators
from superclub.apps.comments.decorators import post_comment_list_decorator

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Utils
from superclub.utils.decorators import token_patch_decorator

# Mixins
from superclub.apps.comments.api.views.mixins.like import CommentLikeViewMixin
from superclub.apps.comments.api.views.mixins.report import CommentReportViewMixin

# Serializers
from superclub.apps.comments.api.serilalizers.list import CommentListSerializer

# Models
from superclub.apps.comments.models.index import Comment


# Class Section
class CommentViewSet(CommentLikeViewMixin,
                     CommentReportViewMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    serializers = {
        'default': CommentListSerializer,
    }
    queryset = Comment.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**token_patch_decorator(title='9. 댓글 - Member'))
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CommentsViewSet(mixins.ListModelMixin,
                      GenericViewSet):
    serializers = {
        'default': CommentListSerializer,
    }
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Comment.objects.filter(post=self.kwargs["post_pk"], parent_comment=None)
        return queryset

    @swagger_auto_schema(**post_comment_list_decorator(title=_('7. 게시판 - Guest'), serializer=CommentListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
