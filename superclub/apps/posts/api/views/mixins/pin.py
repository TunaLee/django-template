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
from superclub.apps.pins.decorators import post_pin_decorator, post_unpin_decorator

# Serializers
from superclub.apps.pins.api.serializers.list import PostPinListSerializer

# Models
from superclub.apps.pins.models.index import PostPin


# Class Section
class PostPinViewMixin:
    @swagger_auto_schema(**post_pin_decorator(title='7. 게시판 - Guest', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='pin', url_name='post_pin')
    def post_pin(self, request, pk=None):
        post = self.get_object()
        instance = request.user.pin_post(post)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=PostPinListSerializer(instance=instance).data
        )

    @swagger_auto_schema(**post_unpin_decorator(title='7. 게시판 - Guest', request_body=no_body))
    @action(detail=True, methods=['post'], url_path='unpin', url_name='post_unpin')
    def post_unpin(self, request, pk=None):
        post = self.get_object()
        instance = post.post_pins.filter(user=request.user).first()
        if not instance:
            raise CustomBadRequestError('핀 객체가 없습니다.')
        instance.is_active = False
        instance.save()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=PostPinListSerializer(instance=instance).data
        )
