# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Utils
from superclub.utils.api.response import Response
from superclub.utils.exception_handlers import CustomBadRequestError

# Decorators
from superclub.apps.pins.decorators import club_pin_decorator, club_unpin_decorator

# Serializers
from superclub.apps.pins.api.serializers.list import ClubPinListSerializer

# Models
from superclub.apps.pins.models.index import ClubPin


# Class Section
class ClubPinViewMixin:
    @swagger_auto_schema(**club_pin_decorator(title='4. 클럽 - Guest', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='pin', url_name='club_pin')
    def club_pin(self, request, pk=None):
        club = self.get_object()
        instance = request.user.pin_club(club)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=ClubPinListSerializer(instance=instance).data
        )

    @swagger_auto_schema(**club_unpin_decorator(title='4. 클럽 - Guest', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='unpin', url_name='club_unpin')
    def club_unpin(self, request, pk=None):
        club = self.get_object()
        instance = ClubPin.objects.filter(club=club, user=request.user).first()
        if not instance:
            raise CustomBadRequestError('핀 객체가 없습니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=ClubPinListSerializer(instance=instance).data
        )
