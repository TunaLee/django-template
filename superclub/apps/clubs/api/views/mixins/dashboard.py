# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.clubs.decorators import club_dashboard_decorator
from rest_framework.decorators import action

# Serializers
from superclub.apps.clubs.api.serializers.index import ClubDashboardSerializer

# Models
from superclub.apps.clubs.models import Club


class ClubDashboardViewMixin:
    @swagger_auto_schema(**club_dashboard_decorator(title='4. 클럽 - Admin', serializer=ClubDashboardSerializer))
    @action(methods=['get'], detail=True, url_path='dashboard', url_name='club_dashboard')
    def club_dashboard(self, request, pk):
        club = Club.objects.get(id=pk)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=ClubDashboardSerializer(instance=club).data
        )
