# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Serializers
from superclub.apps.clubs.api.serializers.list import ClubListSerializer
from superclub.apps.users.api.serializers import UserSerializer

# Models
from superclub.apps.boards.models import BoardGroup
from superclub.apps.clubs.models import Club
from superclub.apps.profiles.models.index import Profile
from superclub.apps.boards.models.index import Board


@receiver(post_save, sender=Club)
def club_post_save(sender, instance, created, **kwargs):
    if created:
        # 클럽 생성 시, 마스터 데이터 삽입, master도 멤버니까 멤버 카운트 + 1
        instance.user_data = UserSerializer(instance=instance.user).data
        instance.member_count = 1
        instance.save()
        # 클럽 생성 시, 마스터의 클럽 프로필 생성
        Profile.objects.create(club=instance, user=instance.user, staff=10, staff_name='MASTER', is_staff=True, user_data=UserSerializer(instance=instance.user).data)

        # 클럽 생성 시, 기본 보드 그룹, 보드 생성
        basic_board_group = BoardGroup.objects.create(name='Basic', club=instance, type='DEFAULT')
        Board.objects.create(club=instance, board_group=basic_board_group, name='All', read_permission=0, write_permission=1, view_mode='LIST_TYPE', type='ALL')
        Board.objects.create(club=instance, board_group=basic_board_group, name='Notice', read_permission=0, write_permission=10, view_mode='LIST_TYPE', type='NOTICE')
        Board.objects.create(club=instance, board_group=basic_board_group, name='Event', read_permission=0, write_permission=10, view_mode='LIST_TYPE', type='EVENT')
        Board.objects.create(club=instance, board_group=basic_board_group, name='Video', read_permission=0, write_permission=1, view_mode='LIST_TYPE', type='VIDEO')
        Board.objects.create(club=instance, board_group=basic_board_group, name='Gallery', read_permission=0, write_permission=1, view_mode='LIST_TYPE', type='GALLERY')

    profile = instance.profile_image
    banner = instance.banner_image
    thumbnail = instance.thumbnail_image

    club = Club.objects.filter(id=instance.pk)

    if profile:
        club.update(profile_image_url=instance.profile_image.url)
    if banner:
        club.update(banner_image_url=instance.banner_image.url)
    if thumbnail:
        club.update(thumbnail_image_url=instance.thumbnail_image.url)

    # TODO: 클럽 수정시, 조인 객체 수정 (호출 될 때마다 수정 되기 때문에 개선 요망)
    instance.joins.update(club_data=ClubListSerializer(instance=instance).data)
