# Django
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Max

# Serializers
from superclub.apps.boards.api.serializers.list import BoardGroupListSerializer

# Models
from superclub.apps.boards.models import BoardGroup, Board


@receiver(post_save, sender=BoardGroup)
def board_group_post_save(sender, instance, created, **kwargs):
    # 클럽에 엮인 보드 그룹의 order 최대 값 + 1
    if created:
        max_board_group = instance.club.board_groups.aggregate(order=Max('order'))
        if not max_board_group['order']:
            max_board_group['order'] = 0
        total_num = max_board_group['order'] + 1
        instance.order = total_num
        instance.save()

    club = instance.club
    club.board_data = BoardGroupListSerializer(club.board_groups, many=True).data
    club.save()


@receiver(post_delete, sender=BoardGroup)
def board_group_post_delete(sender, instance, *args, **kwargs):
    club = instance.club
    club.board_data = BoardGroupListSerializer(club.board_groups, many=True).data
    club.save()


@receiver(post_save, sender=Board)
def board_post_save(sender, instance, created, **kwargs):
    # 보드 그룹에 엮인 보드의 order 최대 값 + 1
    if created:
        max_board = instance.board_group.boards.aggregate(order=Max('order'))
        if not max_board['order']:
            max_board['order'] = 0
        total_num = max_board['order'] + 1
        instance.order = total_num
        instance.save()

    club = instance.board_group.club
    club.board_data = BoardGroupListSerializer(club.board_groups, many=True).data
    club.save()


@receiver(post_delete, sender=Board)
def board_post_delete(sender, instance, *args, **kwargs):
    club = instance.board_group.club
    club.board_data = BoardGroupListSerializer(club.board_groups, many=True).data
    club.save()
