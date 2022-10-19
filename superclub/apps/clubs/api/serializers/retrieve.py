# Django Rest Framework
from rest_framework import serializers

# Local
from superclub.apps.club_tags.api.serializers.list import ClubTagListSerializer
from superclub.apps.clubs.models import Club
from superclub.apps.profiles.api.serializers.list import ProfileListSerializer
from superclub.apps.users.api.serializers import UserSerializer
from superclub.bases.api.serializers import ModelSerializer


class ClubRetrieveSerializer(ModelSerializer):
    tags = serializers.SerializerMethodField()
    master = serializers.JSONField(source='user_data')
    board_groups = serializers.JSONField(source='board_data')
    profile = serializers.SerializerMethodField()
    is_pin = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = ('id', 'category', 'master', 'profile',
                  'profile_image', 'profile_image_url', 'banner_image', 'banner_image_url',
                  'is_pin', 'name', 'address', 'description', 'is_auto_approval', 'tags',
                  'member_count', 'post_count', 'pin_count',
                  'board_groups')

    def get_tags(self, obj):
        instance = obj.club_tags.order_by('order')
        return ClubTagListSerializer(instance=instance, many=True).data

    def get_profile(self, obj):
        user = self.context['request'].user
        if not user.id:
            return None
        profile = obj.profiles.filter(user=user).first()
        if not profile:
            return UserSerializer(instance=user).data
        return ProfileListSerializer(instance=profile).data

    def get_is_pin(self, obj):
        request = self.context.get('request', None)
        if not request:
            return None
        user = request.user
        if not user.id:
            return None
        club_pin = obj.club_pins.filter(user=request.user, is_active=True).first()
        if not club_pin:
            return False
        return True
