# Django Rest Framework
from rest_framework import serializers

# Local
from superclub.apps.joins.models.index import Join
from superclub.bases.api.serializers import ModelSerializer


class JoinSerializer(ModelSerializer):
    class Meta:
        model = Join
        fields = '__all__'
