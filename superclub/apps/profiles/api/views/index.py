# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from superclub.apps.profiles.api.serializers.list import ProfileListSerializer

# Models
from superclub.apps.profiles.models.index import Profile

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Utils
from superclub.utils.decorators import token_retrieve_decorator


class ProfileViewSet(mixins.RetrieveModelMixin,
                     GenericViewSet):
    serializers = {
        'default': ProfileListSerializer,
    }
    queryset = Profile.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**token_retrieve_decorator(title=_('8. 프로필 - Member'), serializer=ProfileListSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)
