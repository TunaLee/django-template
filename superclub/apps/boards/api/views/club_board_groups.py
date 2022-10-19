# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Bases
from superclub.bases.api import mixins
from superclub.bases.api.viewsets import GenericViewSet

# Decorators
from superclub.apps.boards.decorators import club_board_group_list_decorator

# Serializers
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer

# Models
from superclub.apps.boards.models import BoardGroup


# Class Section
class ClubBoardGroupsViewSet(mixins.ListModelMixin,
                             GenericViewSet):
    serializers = {
        'default': BoardGroupListSerializer,
    }
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = BoardGroup.objects.filter(club=self.kwargs["club_pk"])
        return queryset

    @swagger_auto_schema(**club_board_group_list_decorator(title=_('4. 클럽 - Guest'), serializer=BoardGroupListSerializer))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
