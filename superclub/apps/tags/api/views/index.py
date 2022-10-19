# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Permission
from superclub.apps.tags.api.serializers.list import TagListSerializer
from superclub.apps.tags.models import Tag

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Decorators
from superclub.utils.decorators import list_decorator


# Class Section
class TagsViewSet(mixins.ListModelMixin,
                  GenericViewSet):
    serializers = {
        'default': TagListSerializer,
    }
    queryset = Tag.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**list_decorator(title=_('3. 태그 - Guest'), serializer=TagListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
