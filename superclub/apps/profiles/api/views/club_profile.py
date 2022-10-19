# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# DRF
from rest_framework.filters import SearchFilter

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Filters
from superclub.apps.profiles.api.views.filters.profiles_filter import ProfilesFilter

# Serializers
from superclub.apps.profiles.api.serializers.list import ProfileListSerializer

# Decorators
from superclub.apps.profiles.decorators import club_profile_list_decorator

# Models
from superclub.apps.profiles.models.index import Profile

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet


class ClubProfilesViewSet(mixins.ListModelMixin,
                          GenericViewSet):
    serializers = {
        'default': ProfileListSerializer,
    }
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('user__username',)
    filter_class = ProfilesFilter

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = Profile.objects.filter(club=self.kwargs["club_pk"])
        # TODO 비활성화 된 유저 필터링
        # TODO Ordering 정책 반영
        # TODO 접속중인 유저 + 친구
        # TODO 접속중인 유저 + 노친구
        # TODO 미접속중인 유저 + 친구
        # TODO 접속중인 유저 + 노친구
        # TODO 캐싱처리
        return queryset

    @swagger_auto_schema(**club_profile_list_decorator(title=_('4. 클럽 - Member'), serializer=ProfileListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
