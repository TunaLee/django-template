# DRF
from rest_framework import serializers

# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.comments.models.index import Comment


class CommentListSerializer(ModelSerializer):
    profile = serializers.JSONField(source='profile_data')
    child_comment = serializers.JSONField(source='child_comment_data')
    is_like = serializers.SerializerMethodField()
    is_dislike = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'parent_comment', 'club', 'post', 'profile',
                  'content', 'image', 'image_url',
                  'like_count', 'dislike_count',
                  'is_like', 'is_dislike', 'is_secret',
                  'created', 'modified',
                  'child_comment')

    def get_is_like(self, obj):
        request = self.context.get('request', None)
        if not request:
            return None
        user = request.user
        if not user.id:
            return None
        comment_like = obj.comment_likes.filter(user=request.user, is_active=True).first()
        if not comment_like:
            return False
        return True

    def get_is_dislike(self, obj):
        request = self.context.get('request', None)
        if not request:
            return None
        user = request.user
        if not user.id:
            return None
        comment_dislike = obj.comment_dislikes.filter(user=request.user, is_active=True).first()
        if not comment_dislike:
            return False
        return True
