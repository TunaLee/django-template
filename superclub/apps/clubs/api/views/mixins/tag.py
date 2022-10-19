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
from superclub.apps.club_tags.decorators import club_tag_update_decorator

# Serializers
from superclub.apps.clubs.api.serializers.retrieve import ClubRetrieveSerializer
from superclub.apps.clubs.api.serializers.update import ClubTagUpdateSerializer


class ClubTagViewMixin:
    @swagger_auto_schema(**club_tag_update_decorator(title='4. 클럽 - Admin', request_body=ClubTagUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='tags', url_name='club_tag')
    def club_tag(self, request, pk=None):
        user = request.user
        club = self.get_object()
        tags = request.data['tags']
        if club.user == user:
            club.update_club_tag(tags)
            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message=_('ok'),
                data=ClubRetrieveSerializer(instance=club, context={'request': request}).data
            )
        raise PermissionError('Bad request')
