# Local
from superclub.apps.pins.models.index import ClubPin, PostPin
from superclub.bases.api.serializers import ModelSerializer


class ClubPinActiveSerializer(ModelSerializer):
    class Meta:
        model = ClubPin
        fields = ('id', 'is_active',)


class PostPinActiveSerializer(ModelSerializer):
    class Meta:
        model = PostPin
        fields = ('id', 'is_active',)
