# Bases
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.likes.models import PostLike, CommentLike


# Class Section
class PostLikeListSerializer(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('id', 'post', 'profile_data', 'created', 'modified')


class CommentLikeListSerializer(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ('id', 'comment', 'profile', 'created', 'modified')
