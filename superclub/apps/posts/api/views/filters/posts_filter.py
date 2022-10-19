# Django
import django_filters
from django_filters import CharFilter, NumberFilter, OrderingFilter

# Models
from superclub.apps.posts.models import Post


# TODO is_liked, is_commented 개발하기
class PostsFilter(django_filters.FilterSet):
    profile = NumberFilter(field_name='profile')
    board = NumberFilter(field_name='board')
    tag_name = CharFilter(field_name='post_tags__tag__name')
    is_image = CharFilter(method='is_image_filter')
    is_video = CharFilter(method='is_video_filter')
    is_temporary = CharFilter(method='is_temporary_filter')
    is_notice = CharFilter(method='is_notice_filter')
    is_event = CharFilter(method='is_event_filter')
    is_active = CharFilter(method='is_active_filter')
    # is_liked = CharFilter(method='is_liked_filter')
    # is_commented = CharFilter(method='is_commented_filter')

    class Meta:
        model = Post
        fields = ['profile', 'board', 'tag_name',
                  'is_image', 'is_video',
                  'is_notice', 'is_event', 'is_active',
                  'is_temporary']

    def is_image_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_image=True)

    def is_video_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_video=True)

    def is_temporary_filter(self, queryset, name, value):
        if value == 'true':
            user = self.request.user
            return queryset.filter(user=user, is_temporary=True)

    def is_notice_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_notice=True)

    def is_event_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_event=True)

    def is_active_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_active=True)
        elif value == 'false':
            return queryset.filter(is_active=False)

    # def is_liked_filter(self, queryset, name, value):
    #
    # def is_commented_filter(self, queryset, name, value):


class PostsAdminFilter(django_filters.FilterSet):
    board = NumberFilter(field_name='board')

    class Meta:
        model = Post
        fields = ['board', 'is_active']

    def is_active_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_active=True)
        elif value == 'false':
            return queryset.filter(is_active=False)
