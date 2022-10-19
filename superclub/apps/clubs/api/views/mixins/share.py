# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.shares.decorators import club_share_decorator

# Serializers
from superclub.apps.shares.api.serializers.list import ClubShareListSerializer
from superclub.apps.shares.api.serializers.create import ClubShareCreateSerializer


# Class Section
class ClubShareViewMixin:
    @swagger_auto_schema(**club_share_decorator(title='4. 클럽 - Guest', request_body=ClubShareCreateSerializer))
    @action(detail=True, methods=['post'], url_path='share', url_name='club_share')
    def club_share(self, request, pk=None):
        club = self.get_object()
        link = request.data['link']
        instance = request.user.share_club(club, link)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=ClubShareListSerializer(instance=instance).data
        )
