# Django Rest Framework
from rest_framework import serializers

# Models
from superclub.apps.posts.models.index import Post

# API
from superclub.bases.api.serializers import ModelSerializer


# TODO Detail Image Update 로직 구현하기
# Class Section
class PostUpdateSerializer(ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(allow_blank=False), required=False)

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags', 'password',
                  'is_temporary', 'is_secret',
                  'is_notice', 'is_event',
                  'is_comment', 'is_share', 'is_search')

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        user = self.context["request"].user
        validated_data["user"] = user
        instance.update(**validated_data)
        instance.update_post_tag(tags)
        return instance


class PostTagUpdateSerializer(ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Post
        fields = ('tags',)


class PostActiveSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('is_active',)


class PostsActiveSerializer(ModelSerializer):
    id = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Post
        fields = ('id',)
