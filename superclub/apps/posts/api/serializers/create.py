# Django Rest Framework
from rest_framework import serializers

# Serializers
from superclub.apps.posts.api.serializers.index import PostImageSerializer

# Models
from superclub.apps.posts.models.index import Post

# API
from superclub.bases.api.serializers import ModelSerializer
from superclub.utils.api.fields import HybridImageField


# Class Section
class PostCreateSerializer(ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    thumbnail_image = HybridImageField(use_url=True, required=False)
    tags = serializers.ListField(required=False, child=serializers.CharField(allow_blank=True))

    class Meta:
        model = Post
        fields = ('thumbnail_image', 'board', 'title', 'content', 'images', 'tags',
                  'is_temporary', 'is_secret', 'password',
                  'is_notice', 'is_event', 'is_search', 'is_share', 'is_comment')
