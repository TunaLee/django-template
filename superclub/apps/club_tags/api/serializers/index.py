# Local
from superclub.apps.club_tags.models.index import ClubTag
from superclub.bases.api.serializers import ModelSerializer


class ClubTagSerializer(ModelSerializer):
    class Meta:
        model = ClubTag
        fields = '__all__'
