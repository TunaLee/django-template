# Local
from superclub.apps.shares.models.index import ClubShare, PostShare
from superclub.bases.api.serializers import ModelSerializer


class ClubShareListSerializer(ModelSerializer):
    class Meta:
        model = ClubShare
        fields = ('id', 'user', 'club', 'link')


class PostShareListSerializer(ModelSerializer):
    class Meta:
        model = PostShare
        fields = ('id', 'user', 'post', 'link')
