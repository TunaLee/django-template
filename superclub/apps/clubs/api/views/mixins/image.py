# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.clubs.decorators import club_profile_image_update_decorator, club_banner_image_update_decorator

# Serializers
from superclub.apps.clubs.api.serializers.update import ProfileImageUpdateSerializer, ClubBannerImageUpdateSerializer


class ClubImageViewMixin(GenericAPIView):
    @swagger_auto_schema(**club_profile_image_update_decorator(title='4. 클럽 - Admin',
                                                               request_body=ProfileImageUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='profile-image', url_name='club_profile_image')
    def club_profile_image(self, request, pk=None):
        user = request.user
        club = self.get_object()
        data = request.data
        if club.user == user:
            serializer = ProfileImageUpdateSerializer(instance=club, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    status=status.HTTP_200_OK,
                    code=200,
                    message=_('ok'),
                    data=serializer.data
                )
        raise PermissionError('Bad request')

    @swagger_auto_schema(**club_banner_image_update_decorator(title='4. 클럽 - Admin',
                                                              request_body=ClubBannerImageUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='banner-image', url_name='club_banner_image')
    def club_banner_image(self, request, pk=None):
        user = request.user
        club = self.get_object()
        data = request.data
        if club.user == user:
            serializer = ClubBannerImageUpdateSerializer(instance=club, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    status=status.HTTP_200_OK,
                    code=200,
                    message=_('ok'),
                    data=serializer.data
                )
        raise PermissionError('Bad request')
