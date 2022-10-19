# Django Rest Framework
from rest_framework import serializers

from superclub.apps.pins.api.serializers.index import PostPinActiveSerializer
# Serializers
from superclub.apps.posts.api.serializers.index import PostImageSerializer
from superclub.apps.post_tags.api.serializers.list import PostTagListSerializer

# Models
from superclub.apps.posts.models.index import Post

# API
from superclub.bases.api.serializers import ModelSerializer


# Class Section
class PostRetrieveSerializer(ModelSerializer):
    profile = serializers.JSONField(source='profile_data')
    detail_images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    is_pin = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()
    is_dislike = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'club', 'board_group', 'board_group_name', 'board', 'board_name',
                  'profile',
                  'content', 'title', 'detail_images', 'password', 'tags',
                  'comment_count', 'view_count', 'like_count', 'dislike_count',
                  'is_pin', 'is_like', 'is_dislike',
                  'is_temporary', 'is_secret', 'is_search', 'is_share', 'is_comment',
                  'is_notice', 'is_event', 'is_image', 'is_video',
                  'created', 'modified')

    def get_detail_images(self, obj):
        return PostImageSerializer(obj.post_images, many=True).data

    def get_tags(self, obj):
        instance = obj.post_tags.order_by('order')
        return PostTagListSerializer(instance=instance, many=True).data

    def get_is_pin(self, obj):
        user = self.context['request'].user
        if not user.id:
            return None
        post_pin = obj.post_pins.filter(user=user, is_active=True).first()
        if not post_pin:
            return False
        return True

    def get_is_like(self, obj):
        user = self.context['request'].user
        if not user.id:
            return None
        post_like = obj.post_likes.filter(user=user, is_active=True).first()
        if not post_like:
            return False
        return True

    def get_is_dislike(self, obj):
        user = self.context['request'].user
        if not user.id:
            return None
        post_dislike = obj.post_dislikes.filter(user=user, is_active=True).first()
        if not post_dislike:
            return False
        return True
