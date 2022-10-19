# Bases
from superclub.bases.api.serializers import ModelSerializer

# Utils
from superclub.utils.api.fields import HybridImageField

# Models
from superclub.apps.comments.models.index import Comment


# Class Section
class CommentCreateSerializer(ModelSerializer):
    image = HybridImageField(use_url=True, required=False)

    class Meta:
        model = Comment
        fields = ('parent_comment', 'content', 'image', 'is_secret')
