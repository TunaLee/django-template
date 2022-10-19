# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from superclub.apps.likes.api.serializers.list import PostLikeListSerializer

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Decorators
from superclub.apps.likes.decorators import post_like_list_decorator

# Models
from superclub.apps.likes.models import PostLike


# Class Section
class PostLikesViewSet(mixins.ListModelMixin,
                       GenericViewSet):
    serializers = {
        'default': PostLikeListSerializer,
    }
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = PostLike.active.filter(post=self.kwargs["post_pk"])
        return queryset

    @swagger_auto_schema(**post_like_list_decorator(title=_('7. 게시판 - Member'), serializer=PostLikeListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
