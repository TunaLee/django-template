# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Local
from superclub.apps.categories.api.serializers.list import CategoryListSerializer
from superclub.apps.categories.models.index import Category
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet
from superclub.utils.decorators import list_decorator


class CategoriesViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    serializers = {
        'default': CategoryListSerializer,
    }
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**list_decorator(title=_('2. 카테고리 - Guest'), serializer=CategoryListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
