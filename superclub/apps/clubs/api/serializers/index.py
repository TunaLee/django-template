# Django Rest Framework
from rest_framework import serializers

# Bases
from superclub.bases.api.serializers import ModelSerializer

# Local
from superclub.apps.clubs.models import Club


class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class ClubCheckNameSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = ('name',)


class ClubCheckAddressSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = ('address',)


class ClubDashboardSerializer(ModelSerializer):
    daily_post_count = serializers.SerializerMethodField()
    daily_view_count = serializers.SerializerMethodField()
    daily_comment_count = serializers.SerializerMethodField()
    daily_member_count = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = (
            'post_count', 'view_count', 'comment_count', 'member_count',
            'daily_post_count',
            'daily_view_count', 'daily_comment_count', 'daily_member_count'
        )

    def get_daily_post_count(self, obj):
        return obj.get_daily_post_count()

    def get_daily_view_count(self, obj):
        return obj.get_daily_view_count()

    def get_daily_comment_count(self, obj):
        return obj.get_daily_comment_count()

    def get_daily_member_count(self, obj):
        return obj.get_daily_member_count()
