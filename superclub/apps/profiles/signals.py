# Django
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Serializers
from superclub.apps.users.api.serializers import UserSerializer

# Models
from superclub.apps.profiles.models.index import Profile


@receiver(pre_save, sender=Profile)
def profile_pre_save(sender, instance, *args, **kwargs):
    instance.user_data = UserSerializer(instance=instance.user).data
