# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.exception_handlers import CustomBadRequestError
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.clubs.decorators import club_check_name_create_decorator, club_check_address_create_decorator

# Serializers
from superclub.apps.clubs.api.serializers.index import ClubCheckNameSerializer, ClubCheckAddressSerializer

# Models
from superclub.apps.clubs.models import Club


# Class Section
class ClubCreateViewMixin:
    @swagger_auto_schema(**club_check_name_create_decorator(title=_('4. 클럽 - Admin'), request_body=ClubCheckNameSerializer))
    @action(methods=['post'], detail=False, url_path='name/check', url_name='check_name')
    def check_new_name(self, request):
        name = request.data.get('name')
        if Club.objects.filter(name=name).exists():
            raise CustomBadRequestError('Already in use. Please enter a different name.')
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('Available'),
        )

    @swagger_auto_schema(
        **club_check_address_create_decorator(title=_('4. 클럽 - Admin'), request_body=ClubCheckAddressSerializer))
    @action(methods=['post'], detail=False, url_path='address/check', url_name='check_address')
    def check_new_address(self, request):
        address = request.data.get('address')
        if Club.objects.filter(address=address).exists():
            raise CustomBadRequestError('Already in use. Please enter a different address.')
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('Available'),
        )
