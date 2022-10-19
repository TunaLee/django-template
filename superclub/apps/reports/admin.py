from django.contrib import admin

from superclub.apps.reports.models import PostReport
from superclub.bases.admin import Admin


@admin.register(PostReport)
class PostReportAdmin(Admin):
    list_display = ('post', 'profile', 'content')

    # readonly_fields = ('comment', 'user')

    fieldsets = (
        ("정보", {"fields": ('post', 'profile', 'content')}),
    )
