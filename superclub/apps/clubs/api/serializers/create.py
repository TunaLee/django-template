# Django Rest Framework
from rest_framework import serializers

# Utils
from superclub.utils.api.fields import HybridImageField

# Local
from superclub.apps.clubs.models import Club
from superclub.bases.api.serializers import ModelSerializer


class ClubCreateSerializer(ModelSerializer):
    profile_image = HybridImageField(use_url=True, required=False)
    banner_image = HybridImageField(use_url=True, required=False)
    thumbnail_image = HybridImageField(use_url=True, required=False)
    tags = serializers.ListField(required=False, child=serializers.CharField(allow_blank=True))

    class Meta:
        model = Club
        fields = ('category', 'thumbnail_image', 'profile_image', 'banner_image', 'name', 'description', 'address', 'tags',
                  'is_auto_approval')

    def create(self, validated_data):
        tags = validated_data.pop('tags', None)
        user = self.context["request"].user
        validated_data["user"] = user
        club = Club.objects.create(**validated_data)
        for index, tag in enumerate(tags):
            if tag == "":
                pass
            else:
                club.set_club_tag(index=index, tag=tag)
        return club
