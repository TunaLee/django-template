from django.contrib import admin

from superclub.apps.likes.models.index import CommentLike, CommentDislike, PostLike, PostDislike
from superclub.bases.admin import CountAdmin


@admin.register(CommentLike)
class CommentLikeAdmin(CountAdmin):
    list_display = ('comment', 'user')
    search_fields = ('comment__post', 'user__email')
    # readonly_fields = ('comment', 'user')

    fieldsets = (
        ("정보", {"fields": ('comment', 'user')}),
    )


@admin.register(CommentDislike)
class CommentDislikeAdmin(CountAdmin):
    list_display = ('comment', 'user')
    search_fields = ('comment__post', 'user__email')
    # readonly_fields = ('comment', 'user')

    fieldsets = (
        ("정보", {"fields": ('comment', 'user')}),
    )


@admin.register(PostLike)
class PostLikeAdmin(CountAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__email')
    # readonly_fields = ('post', 'user')

    fieldsets = (
        ("정보", {"fields": ('post', 'user')}),
    )


@admin.register(PostDislike)
class PostDislikeAdmin(CountAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__email')
    # readonly_fields = ('post', 'user')

    fieldsets = (
        ("정보", {"fields": ('post', 'user')}),
    )
