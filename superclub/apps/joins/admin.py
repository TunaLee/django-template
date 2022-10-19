from django.contrib import admin

from superclub.apps.joins.models.index import Join
from superclub.bases.admin import Admin


@admin.register(Join)
class JoinAdmin(Admin):
    list_display = ('club', 'user')
    search_fields = ('club__name', 'user__email')
    # readonly_fields = ('club', 'user')
    fieldsets = (
        ("정보", {"fields": ('club', 'user')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('club', 'user')}),
    )
