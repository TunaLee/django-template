# Serializers
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.boards.models import BoardGroup, Board


# Class Section
class BoardGroupSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = '__all__'
