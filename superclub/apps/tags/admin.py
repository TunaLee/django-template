from django.contrib import admin

from superclub.apps.tags.models.index import Tag
from superclub.bases.admin import CountAdmin


@admin.register(Tag)
class TagAdmin(CountAdmin):
    list_display = ('name', 'club_count', 'post_count')
    ordering = ('club_count', 'post_count')

    fieldsets = (
        ("1. 정보", {"fields": ('name',)}),
        ("2. 카운트", {"fields": ('club_count', 'post_count')})
    )

    readonly_fields = ('name', 'club_count', 'post_count')
