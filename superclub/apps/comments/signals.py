# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Serializers
from superclub.apps.profiles.api.serializers.list import ProfileListSerializer

# Models
from superclub.apps.comments.models import Comment


@receiver(pre_save, sender=Comment)
def comment_pre_save(sender, instance, *args, **kwargs):
    instance.profile_data = ProfileListSerializer(instance=instance.profile).data
