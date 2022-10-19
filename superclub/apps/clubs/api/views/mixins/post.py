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
from superclub.apps.posts.decorators import club_post_temporary_destroy_decorator
from superclub.apps.clubs.decorators import club_post_create_decorator

# Serializers
from superclub.apps.posts.api.serializers.create import PostCreateSerializer
from superclub.apps.posts.api.serializers.retrieve import PostRetrieveSerializer

# Models
from superclub.apps.clubs.models import Club
from superclub.apps.boards.models import Board
from superclub.apps.posts.models import Post, PostImage


# Class Section
class ClubPostViewMixin:
    @swagger_auto_schema(**club_post_create_decorator(title='4. 클럽 - Member', request_body=PostCreateSerializer))
    @action(detail=True, methods=['post'], url_path='post', url_name='club_post')
    def club_post(self, request, pk=None):
        user = request.user
        club = self.get_object()
        is_temporary = request.data['is_temporary']
        tags = request.data.pop('tags', None)
        board_pk = request.data.pop('board', None)
        board = Board.objects.filter(id=board_pk).first()

        if not board:
            board_name = None
            board_group = None
            board_group_name = None

            if not is_temporary:
                raise CustomBadRequestError('게시판 데이터가 없거나, 권한이 없습니다.')
        else:
            board_name = board.name
            board_group = board.board_group
            board_group_name = board_group.name

        profile = user.profiles.filter(club=club).first()
        instance = Post.objects.create(club=club, club_name=club.name,
                                       user=user, user_email=user.email,
                                       profile=profile,
                                       board=board, board_group=board_group,
                                       board_group_name=board_group_name, board_name=board_name, **request.data)
        # 이미지 생성
        images_data = request.FILES

        for image_data in images_data.getlist('image'):
            PostImage.objects.create(post=instance, image=image_data)
            instance.is_image = True
            instance.save()

        # 태그 생성
        for index, tag in enumerate(tags):
            if tag == "":
                pass
            else:
                instance.set_post_tag(index=index, tag=tag)

        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=PostRetrieveSerializer(instance=instance, context={'request': request}).data
        )

    @swagger_auto_schema(**club_post_temporary_destroy_decorator(title='4. 클럽 - Member'))
    @action(methods=['delete'], detail=True, url_path='posts/temporary', url_name='club_post_temporary')
    def club_post_temporary(self, request, pk):
        club = Club.objects.get(id=pk)
        club.posts.filter(is_temporary=True).delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )
