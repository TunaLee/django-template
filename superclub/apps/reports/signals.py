# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Serializers
from superclub.apps.profiles.api.serializers.list import ProfileListSerializer

# Models
from superclub.apps.reports.models import CommentReport


@receiver(pre_save, sender=CommentReport)
def comment_report_pre_save(sender, instance, *args, **kwargs):
    instance.profile_data = ProfileListSerializer(instance=instance.profile).data


