from django.contrib import admin

from superclub.apps.shares.models.index import ClubShare, PostShare
from superclub.bases.admin import CountAdmin


@admin.register(ClubShare)
class ClubShareAdmin(CountAdmin):
    list_display = ('club', 'user')
    search_fields = ('club__name', 'user__email')


@admin.register(PostShare)
class PostShareAdmin(CountAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user')
