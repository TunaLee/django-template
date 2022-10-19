# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Utils
from superclub.utils.api.response import Response

# Decorators
from superclub.apps.joins.decorators import club_join_decorator, club_leave_decorator

# Serializers
from superclub.apps.joins.api.serializers.list import JoinListSerializer

# Models
from superclub.apps.joins.models.index import Join
from superclub.utils.exception_handlers import CustomBadRequestError


# Class Section
class ClubJoinViewMixin:
    @swagger_auto_schema(**club_join_decorator(title='4. 클럽 - Guest', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='join', url_name='club_join')
    def club_join(self, request, pk=None):
        club = self.get_object()
        instance = request.user.join_club(club)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=JoinListSerializer(instance=instance).data
        )

    @swagger_auto_schema(**club_leave_decorator(title='4. 클럽 - Guest', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='leave', url_name='club_leave')
    def club_leave(self, request, pk=None):
        club = self.get_object()
        instance = Join.objects.filter(club=club, user=request.user).first()
        if not instance:
            raise CustomBadRequestError('클럽 멤버가 아닙니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=JoinListSerializer(instance=instance).data
        )
