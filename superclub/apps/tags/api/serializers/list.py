# Local
from superclub.apps.tags.models.index import Tag
from superclub.bases.api.serializers import ModelSerializer


class TagListSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'club_count', 'post_count')
