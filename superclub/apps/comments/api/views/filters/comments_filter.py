# Django
import django_filters
from django_filters import CharFilter, NumberFilter, OrderingFilter

from superclub.apps.comments.models import Comment


class CommentsAdminFilter(django_filters.FilterSet):
    board = NumberFilter(field_name='board')

    class Meta:
        model = Comment
        fields = ['board', 'is_active']

    def is_active_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_active=True)
        elif value == 'false':
            return queryset.filter(is_active=False)
