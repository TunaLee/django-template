# Local
from superclub.apps.categories.models.index import Category
from superclub.bases.api.serializers import ModelSerializer


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'club_count')
