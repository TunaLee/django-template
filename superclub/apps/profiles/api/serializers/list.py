# Django Rest Framework
from rest_framework import serializers

# Local
from superclub.apps.profiles.models.index import Profile
from superclub.bases.api.serializers import ModelSerializer


class ProfileListSerializer(ModelSerializer):
    user = serializers.JSONField(source='user_data')

    class Meta:
        model = Profile
        fields = ('id', 'club', 'user',
                  'post_count', 'comment_count', 'visit_count',
                  'point', 'level',
                  'grade', 'grade_name', 'staff', 'staff_name')
