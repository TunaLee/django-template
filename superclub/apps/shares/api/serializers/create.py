# Local
from superclub.apps.shares.models.index import ClubShare, PostShare
from superclub.bases.api.serializers import ModelSerializer


# Class Section
class ClubShareCreateSerializer(ModelSerializer):
    class Meta:
        model = ClubShare
        fields = ('link',)


# Class Section
class PostShareCreateSerializer(ModelSerializer):
    class Meta:
        model = PostShare
        fields = ('link',)
