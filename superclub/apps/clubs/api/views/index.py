# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework.filters import OrderingFilter
from rest_framework import status

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Filters
from superclub.apps.clubs.api.views.filters.clubs_filter import ClubsFilter
from superclub.apps.clubs.api.views.filters.clubs_search import ClubsSearchFilter
from superclub.apps.clubs.api.views.mixins.post import ClubPostViewMixin

# API
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet
from superclub.utils.api.response import Response

# Utils
from superclub.utils.decorators import token_create_decorator, retrieve_decorator, list_decorator, token_patch_decorator

# Serializers
from superclub.apps.clubs.api.serializers.create import ClubCreateSerializer
from superclub.apps.clubs.api.serializers.list import ClubListSerializer
from superclub.apps.clubs.api.serializers.retrieve import ClubRetrieveSerializer
from superclub.apps.clubs.api.serializers.update import ClubUpdateSerializer

# Mixins
from superclub.apps.clubs.api.views.mixins.create import ClubCreateViewMixin
from superclub.apps.clubs.api.views.mixins.dashboard import ClubDashboardViewMixin
from superclub.apps.clubs.api.views.mixins.image import ClubImageViewMixin
from superclub.apps.clubs.api.views.mixins.join import ClubJoinViewMixin
from superclub.apps.clubs.api.views.mixins.update import ClubUpdateViewMixin
from superclub.apps.clubs.api.views.mixins.pin import ClubPinViewMixin
from superclub.apps.clubs.api.views.mixins.share import ClubShareViewMixin
from superclub.apps.clubs.api.views.mixins.board_group import ClubBoardGroupViewMixin
from superclub.apps.clubs.api.views.mixins.tag import ClubTagViewMixin

# Models
from superclub.apps.clubs.models import Club


# Class Section
class ClubViewSet(mixins.RetrieveModelMixin,
                  ClubJoinViewMixin,
                  ClubPinViewMixin,
                  ClubShareViewMixin,
                  ClubPostViewMixin,
                  GenericViewSet):
    serializers = {
        'default': ClubRetrieveSerializer,
        'create': ClubCreateSerializer,
        'partial_update': ClubUpdateSerializer
    }
    queryset = Club.objects.all()
    filter_backends = (DjangoFilterBackend,)

    # permission_classes = [ClubPermission]

    @swagger_auto_schema(**retrieve_decorator(title=_('4. 클럽 - Guest'), serializer=ClubRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)


# TODO 심화 검색 기능 만들기 ex)search=a&search_or=b,c&search_exclude=d,e&search_and=f,g,h
class ClubsViewSet(mixins.ListModelMixin,
                   GenericViewSet):
    serializers = {
        'default': ClubListSerializer,
    }
    queryset = Club.objects.all()
    filter_backends = (ClubsSearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ClubsFilter
    search_fields = ('name', 'description', 'address', 'club_tags__name')
    ordering_fields = ('popularity',)

    @swagger_auto_schema(**list_decorator(title=_('4. 클럽 - Guest'), serializer=ClubListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class ClubAdminViewSet(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       ClubDashboardViewMixin,
                       ClubImageViewMixin,
                       ClubUpdateViewMixin,
                       ClubBoardGroupViewMixin,
                       ClubTagViewMixin,
                       GenericViewSet):
    serializers = {
        'default': ClubCreateSerializer,
        'partial_update': ClubUpdateSerializer
    }
    queryset = Club.objects.all()
    filter_backends = (DjangoFilterBackend,)

    # permission_classes = [ClubPermission]

    @swagger_auto_schema(**token_patch_decorator(title='4. 클럽 - Admin'))
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**token_create_decorator(title='4. 클럽 - Admin'))
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = self.perform_create(serializer)
            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message=_('ok'),
                data=ClubRetrieveSerializer(instance=instance, context={'request': request}).data
            )


class ClubsAdminViewSet(ClubCreateViewMixin,
                        GenericViewSet):
    queryset = Club.objects.all()
    filter_backends = (DjangoFilterBackend,)
