# Django
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Serializers
from superclub.apps.clubs.api.serializers.list import ClubListSerializer

# Models
from superclub.apps.joins.models.index import Join
from superclub.apps.profiles.models.index import Profile


# 조인 객체 생성 전에 실행되는 pre_save 로직
@receiver(pre_save, sender=Join)
def join_count_pre_save(sender, instance, *args, **kwargs):
    instance.club_data = ClubListSerializer(instance=instance.club).data


@receiver(post_save, sender=Join)
def join_count_post_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(club=instance.club, user=instance.user)
