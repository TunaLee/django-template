# Models
from superclub.apps.posts.models.index import PostImage

# API
from superclub.bases.api.serializers import ModelSerializer


# Class Section
class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('image',)












