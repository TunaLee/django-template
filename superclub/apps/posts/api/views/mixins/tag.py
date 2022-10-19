# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Decorators
from superclub.apps.post_tags.decorators import post_tag_update_decorator

# Serializers
from superclub.apps.posts.api.serializers.retrieve import PostRetrieveSerializer
from superclub.apps.posts.api.serializers.update import PostTagUpdateSerializer

# Utils
from superclub.utils.api.response import Response


# Class Section
class PostTagViewMixin:
    @swagger_auto_schema(**post_tag_update_decorator(title='7. 게시판 - Member', request_body=PostTagUpdateSerializer))
    @action(detail=True, methods=['patch'], url_path='tags', url_name='post_tag')
    def post_tag(self, request, pk=None):
        user = request.user
        post = self.get_object()
        tags = request.data['tags']

        if post.user == user:
            post.update_post_tag(tags=tags)
            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message=_('ok'),
                data=PostRetrieveSerializer(instance=post).data
            )
        raise PermissionError('Bad request')
