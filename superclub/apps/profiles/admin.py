from django.contrib import admin
from superclub.apps.profiles.models import Profile
from superclub.bases.admin import Admin


@admin.register(Profile)
class ProfileAdmin(Admin):
    list_display = ('club_name', 'user_email', 'staff', 'post_count', 'comment_count', 'visit_count',
                    'point', 'level', 'grade')
    list_filter = ('club_name', 'user_email',)

    ordering = ('created',)

    fieldsets = (
        ("1. 정보", {"fields": ('club', 'user',)}),
        ("2. 카운트", {"fields": ('post_count', 'comment_count', 'visit_count')}),
        ("3. 유저 정보", {"fields": ('staff', 'point', 'level', 'grade')})
    )

    add_fieldsets = (
        ("1. 정보", {"fields": ('club', 'user',)}),
        ("2. 카운트", {"fields": ('post_count', 'comment_count', 'visit_count')}),
        ("3. 유저 정보", {"fields": ('staff', 'point', 'level', 'grade')})
    )

    readonly_fields = ('club_name', 'user_email', 'post_count', 'comment_count', 'visit_count',
                       'point', 'level')
