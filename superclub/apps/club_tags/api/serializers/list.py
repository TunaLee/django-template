# Local
from superclub.apps.club_tags.models.index import ClubTag
from superclub.bases.api.serializers import ModelSerializer


class ClubTagListSerializer(ModelSerializer):
    class Meta:
        model = ClubTag
        fields = ('tag', 'name')
