# Django
import django_filters
from django_filters import CharFilter

# Models
from superclub.apps.profiles.models import Profile


class ProfilesFilter(django_filters.FilterSet):
    is_staff = CharFilter(method='is_staff_filter')

    class Meta:
        model = Profile
        fields = ['is_staff']

    def is_staff_filter(self, queryset, name, value):
        if value == 'true':
            return queryset.filter(is_staff=True)
