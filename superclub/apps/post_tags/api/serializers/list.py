# Local
from superclub.bases.api.serializers import ModelSerializer
from superclub.apps.post_tags.models.index import PostTag


class PostTagListSerializer(ModelSerializer):
    class Meta:
        model = PostTag
        fields = ('tag', 'name')
