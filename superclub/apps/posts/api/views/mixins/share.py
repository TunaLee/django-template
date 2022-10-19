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
from superclub.apps.shares.decorators import post_share_decorator

# Serializers
from superclub.apps.shares.api.serializers.list import PostShareListSerializer
from superclub.apps.shares.api.serializers.create import PostShareCreateSerializer


# Class Section
class PostShareViewMixin:
    @swagger_auto_schema(**post_share_decorator(title='7. 게시판 - Guest', request_body=PostShareCreateSerializer))
    @action(detail=True, methods=['post'], url_path='share', url_name='post_share')
    def post_share(self, request, pk=None):
        post = self.get_object()
        link = request.data['link']
        instance = request.user.share_post(post, link)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=PostShareListSerializer(instance=instance).data
        )
