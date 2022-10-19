# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Utils
from superclub.utils.api.fields import HybridImageField

# Models
from superclub.apps.comments.models.index import Comment


class CommentUpdateSerializer(ModelSerializer):
    image = HybridImageField(use_url=True, required=False)

    class Meta:
        model = Comment
        fields = ('content', 'image', 'is_secret')

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        return instance
