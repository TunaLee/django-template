# Django Rest Framework
from rest_framework import serializers

# Serializers
from superclub.apps.post_tags.api.serializers.list import PostTagListSerializer

# Models
from superclub.apps.posts.models.index import Post

# API
from superclub.bases.api.serializers import ModelSerializer


# Class Section
class PostListSerializer(ModelSerializer):
    profile = serializers.JSONField(source='profile_data')
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'club', 'profile',
                  'thumbnail_image', 'thumbnail_image_url',
                  'title', 'content', 'tags',
                  'is_temporary', 'is_secret', 'is_search', 'is_share', 'is_comment',
                  'is_notice', 'is_event', 'is_image', 'is_video',
                  'popularity',
                  'comment_count', 'view_count', 'like_count',
                  'created', 'modified')

    def get_tags(self, obj):
        instance = obj.post_tags.order_by('order')
        return PostTagListSerializer(instance=instance, many=True).data


class PostAdminListSerializer(ModelSerializer):
    profile = serializers.JSONField(source='profile_data')

    class Meta:
        model = Post
        fields = ('id', 'board_name', 'title', 'profile', 'created', 'is_active', 'report_count', 'report_date')
