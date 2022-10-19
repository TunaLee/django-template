# Local
from superclub.apps.categories.models.index import Category
from superclub.bases.api.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
