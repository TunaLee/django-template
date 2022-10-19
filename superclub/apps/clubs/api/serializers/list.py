# Django Rest Framework
from rest_framework import serializers

# Serializers
from superclub.apps.club_tags.api.serializers.list import ClubTagListSerializer

# Bases
from superclub.bases.api.serializers import ModelSerializer

# Models
from superclub.apps.clubs.models import Club


# Class Section
class ClubListSerializer(ModelSerializer):
    tags = serializers.SerializerMethodField()
    is_pin = serializers.SerializerMethodField()
    master = serializers.JSONField(source='user_data')

    class Meta:
        model = Club
        fields = ('id', 'category', 'master',
                  'thumbnail_image', 'thumbnail_image_url', 'profile_image', 'profile_image_url',
                  'name', 'description', 'address', 'tags', 'is_pin', 'member_count')

    def get_tags(self, obj):
        instance = obj.club_tags.order_by('order')
        return ClubTagListSerializer(instance=instance, many=True).data

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
