from django.contrib import admin

from superclub.apps.views.models.index import ClubView, PostView, PostVideoView
from superclub.bases.admin import CountAdmin


@admin.register(ClubView)
class ClubViewAdmin(CountAdmin):
    list_display = ('club', 'user')
    search_fields = ('club__name', 'user__email')
    # readonly_fields = ('club', 'user')

    fieldsets = (
        ("정보", {"fields": ('club', 'user')}),
    )


@admin.register(PostView)
class PostView(CountAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__email')
    # readonly_fields = ('post', 'user')

    fieldsets = (
        ("정보", {"fields": ('post', 'user')}),
    )


@admin.register(PostVideoView)
class PostVideoView(CountAdmin):
    list_display = ('post_video', 'user')
    search_fields = ('post_video__post__title', 'user__email')

    fieldsets = (
        ("정보", {"fields": ('post_video', 'user')}),
    )
