# Local
from superclub.apps.pins.models.index import ClubPin, PostPin
from superclub.bases.api.serializers import ModelSerializer


class ClubPinListSerializer(ModelSerializer):
    class Meta:
        model = ClubPin
        fields = ('id', 'user', 'club', 'is_active')


class PostPinListSerializer(ModelSerializer):
    class Meta:
        model = PostPin
        fields = ('id', 'user', 'post', 'is_active')
