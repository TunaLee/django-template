# Django Rest Framework
from rest_framework import serializers

# Bases
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.reports.models import CommentReport, PostReport


# Class Section
class PostReportListSerializer(ModelSerializer):
    profile = serializers.JSONField(source='profile_data')

    class Meta:
        model = PostReport
        fields = ('id', 'comment', 'profile', 'type', 'content', 'created')


class CommentReportListSerializer(ModelSerializer):
    profile = serializers.JSONField(source='profile_data')

    class Meta:
        model = CommentReport
        fields = ('id', 'comment', 'profile', 'type', 'content', 'created')
