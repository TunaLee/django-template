# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework.filters import SearchFilter, OrderingFilter

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Filters
from superclub.apps.posts.api.views.filters.posts_filter import PostsFilter

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Utils
from superclub.utils.decorators import list_decorator

# Serializers
from superclub.apps.posts.api.serializers.list import PostListSerializer

# Models
from superclub.apps.posts.models.index import Post


# Class Section
class BoardPostsViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    serializers = {
        'default': PostListSerializer,
    }
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = PostsFilter
    search_fields = ('title', 'content', 'post_tags__name')
    ordering_fields = ('popularity',)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Post.objects.filter(board=self.kwargs["board_pk"])
        return queryset

    @swagger_auto_schema(**list_decorator(title=_('6. 게시판 - Guest'), serializer=PostListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
