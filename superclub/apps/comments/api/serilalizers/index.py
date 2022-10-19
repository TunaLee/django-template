# Local
from superclub.apps.comments.models.index import Comment
from superclub.bases.api.serializers import ModelSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
