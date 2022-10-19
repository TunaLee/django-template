from django.contrib import admin

from superclub.apps.club_counts.models.index import ClubDailyViewCount
from superclub.bases.admin import CountAdmin, Admin


@admin.register(ClubDailyViewCount)
class ClubDailyViewCountAdmin(Admin):
    list_display = ('club', 'count', 'date')
    # readonly_fields = ('comment', 'user')
    #
    # fieldsets = (
    #     ("정보", {"fields": ('post', 'date')}),
    # )
