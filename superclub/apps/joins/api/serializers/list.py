# Django Rest Framework
from rest_framework import serializers

# Local
from superclub.apps.joins.models.index import Join
from superclub.bases.api.serializers import ModelSerializer


class JoinListSerializer(ModelSerializer):
    club = serializers.JSONField(source='club_data')

    class Meta:
        model = Join
        fields = ('id', 'user', 'club', 'is_active')
