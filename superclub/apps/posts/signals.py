# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Serializers
from superclub.apps.profiles.api.serializers.list import ProfileListSerializer

# Models
from superclub.apps.posts.models.index import Post


@receiver(post_save, sender=Post)
def post_post_save(sender, instance, created, **kwargs):
    if created:
        instance.profile_data = ProfileListSerializer(instance=instance.profile).data
        instance.save()
    thumbnail_image = instance.thumbnail_image
    post = Post.objects.filter(id=instance.pk)

    if thumbnail_image:
        post.update(thumbnail_image_url=instance.thumbnail_image.url)
