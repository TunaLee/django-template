from django.contrib import admin

from superclub.apps.comments.models.index import Comment
from superclub.bases.admin import Admin


@admin.register(Comment)
class CommentAdmin(Admin):
    list_display = ('post', 'user', 'like_count', 'dislike_count', 'is_secret')
    search_fields = ('post__title', 'user__email',)
    list_filter = ('is_secret',)

    fieldsets = (
        ("1. 정보", {"fields": ('post', 'is_secret')}),
        ("2. 내용", {"fields": ('content',)}),
        ("3. 유저", {"fields": ('user',)}),
        ("4. 좋아요 및 싫어요 수", {
            "fields": ('like_count', 'dislike_count',)
        })
    )

    add_fieldsets = (
        ("Fk", {"fields": ('post', 'user')}),
        ("Main", {"fields": ('content',)}),
        ("Count", {"fields": ('like_count', 'dislike_count',)}),
        ("Boolean", {"fields": ('is_secret',)}),
    )

    readonly_fields = ('like_count', 'dislike_count')
