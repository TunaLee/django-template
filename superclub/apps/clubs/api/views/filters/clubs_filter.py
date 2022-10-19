# Django
import django_filters
from django_filters import NumberFilter, CharFilter

# Models
from superclub.apps.clubs.models import Club


# Class Section
class ClubsFilter(django_filters.FilterSet):
    category = NumberFilter(field_name='category')
    is_joined = CharFilter(method='is_joined_filter')
    is_managing = CharFilter(method='is_managing_filter')

    class Meta:
        model = Club
        fields = ['category', 'is_joined', 'is_managing']

    def is_joined_filter(self, queryset, name, value):
        if value == 'true':
            club_ids = self.request.user.joins.values_list('club_id', flat=True)
            return queryset.filter(id__in=club_ids)

    def is_managing_filter(self, queryset, name, value):
        if value == 'true':
            club_ids = self.request.user.profiles.filter(is_staff=True).values_list('club_id', flat=True)
            return queryset.filter(id__in=club_ids)
