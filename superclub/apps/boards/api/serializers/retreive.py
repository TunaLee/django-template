# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.boards.models import BoardGroup, Board


# Class Section
class BoardGroupRetrieveSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ('id', 'name', 'type', 'is_active')


class BoardRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'description', 'view_mode', 'type', 'read_permission', 'write_permission', 'is_active')
