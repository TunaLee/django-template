# Local
from superclub.apps.users.models import User
from superclub.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_image', 'profile_image_url', 'username')


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_image', 'profile_image_url', 'username', 'join_count', 'post_count', 'comment_count')
