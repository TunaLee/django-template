# Django Rest Framework
from rest_framework import serializers

# Bases
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.reports.models import CommentReport, PostReport


# Class Section
class CommentReportCreateSerializer(ModelSerializer):
    class Meta:
        model = PostReport
        fields = ('type', 'content')
