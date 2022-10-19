# Django Rest Framework
from rest_framework import serializers

# Utils
from superclub.utils.api.fields import HybridImageField

# Local
from superclub.apps.clubs.models import Club
from superclub.bases.api.serializers import ModelSerializer


class ClubUpdateSerializer(ModelSerializer):
    profile_image = HybridImageField(use_url=True, required=False)
    banner_image = HybridImageField(use_url=True, required=False)
    thumbnail_image = HybridImageField(use_url=True, required=False)
    tags = serializers.ListField(child=serializers.CharField(allow_blank=False), required=False)

    class Meta:
        model = Club
        fields = ('category', 'thumbnail_image', 'profile_image', 'banner_image', 'name', 'description', 'address', 'tags',
                  'is_auto_approval')

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        user = self.context["request"].user
        validated_data["user"] = user
        instance.update(**validated_data)
        instance.update_club_tag(tags)
        return instance


class ClubThumbnailImageUpdateSerializer(ModelSerializer):
    thumbnail_image = HybridImageField(use_url=True, required=True)

    class Meta:
        model = Club
        fields = ('thumbnail_image',)


class ProfileImageUpdateSerializer(ModelSerializer):
    profile_image = HybridImageField(use_url=True, required=True)

    class Meta:
        model = Club
        fields = ('profile_image',)


class ClubBannerImageUpdateSerializer(ModelSerializer):
    banner_image = HybridImageField(use_url=True, required=True)

    class Meta:
        model = Club
        fields = ('banner_image',)


class ClubTagUpdateSerializer(ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Club
        fields = ('tags',)
