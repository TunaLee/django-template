# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response
from superclub.utils.exception_handlers import CustomBadRequestError

# Decorators
from superclub.apps.clubs.decorators import club_check_address_update_decorator, club_check_name_update_decorator

# Serializers
from superclub.apps.clubs.api.serializers.index import ClubCheckNameSerializer, ClubCheckAddressSerializer

# Models
from superclub.apps.clubs.models import Club


class ClubUpdateViewMixin:
    @swagger_auto_schema(**club_check_name_update_decorator(title=_('4. 클럽 - Admin'), request_body=ClubCheckNameSerializer))
    @action(methods=['post'], detail=True, url_path='name/check', url_name='check_name')
    def check_changeable_name(self, request, pk=None):
        # Variable Section
        name = request.data.get('name')
        instance = self.get_object()
        if Club.objects.exclude(id=instance.id).filter(name=name).exists():
            raise CustomBadRequestError('Already in use. Please enter a different name.')
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('Available'),
        )

    @swagger_auto_schema(
        **club_check_address_update_decorator(title=_('4. 클럽 - Admin'), request_body=ClubCheckAddressSerializer))
    @action(methods=['post'], detail=True, url_path='address/check', url_name='check_address')
    def check_changeable_address(self, request, pk):
        address = request.data.get('address')
        instance = self.get_object()
        if Club.objects.exclude(id=instance.id).filter(address=address).exists():
            raise CustomBadRequestError('Already in use. Please enter a different address.')
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('Available'),
        )
