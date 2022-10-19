from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from superclub.apps.clubs.models import Club
from superclub.bases.admin import Admin


@admin.register(Club)
class ClubAdmin(Admin):
    list_display = ('name', 'profile_image_tag', 'banner_image_tag', 'category', 'address_reference', 'user_data',
                    'member_count', 'post_count', 'pin_count')
    search_fields = ('category__name', 'user_data', 'address', 'tags')
    list_filter = ('category',)
    ordering = ()

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="100px;"/>'.format(obj.profile_image.url))
    profile_image_tag.short_description = '프로필'

    def banner_image_tag(self, obj):
        if obj.banner_image:
            return format_html('<img src="{}" width="100px;"/>'.format(obj.banner_image.url))
    banner_image_tag.short_description = '배너'

    def address_reference(self, obj):
        return mark_safe(
            f'<a style="display: inline-block; width: 120px; word-wrap:break-word !important;" href="{obj.address}" target="_blank">{obj.address}</a>')
    address_reference.short_description = '웹'

    fieldsets = (
        ("1. 정보", {"fields": ('name', 'description', 'category', 'address')}),
        ("2. 이미지", {"fields": ('profile_image_tag', 'profile_image', 'profile_image_url', 'banner_image_tag', 'banner_image', 'banner_image_url')}),
        ("3. 유저", {"fields": ('user', 'user_data',)}),
        ("4. 전체 통계", {"fields": ('member_count', 'post_count', 'pin_count', 'view_count')}),
        ("5. 일간 통계", {"fields": ('daily_member_count', 'daily_post_count', 'daily_pin_count')}),
        ("6. 주간 통계", {"fields": ('weekly_member_count', 'weekly_post_count', 'weekly_pin_count')}),
        ("7. 월간 통계", {"fields": ('monthly_member_count', 'monthly_post_count', 'monthly_pin_count')}),
        ("8, 클럽 권한", {"fields": ('board_permission', 'merge_permission', )})
    )

    add_fieldsets = (
        ("1. 정보", {"fields": ('name', 'description', 'category', 'address')}),
        ("2. 이미지", {"fields": ('profile_image_tag', 'profile_image', 'profile_image_url', 'banner_image_tag', 'banner_image', 'banner_image_url')}),
        ("3. 유저", {"fields": ('user', 'user_data',)}),
        ("4. 전체 통계", {"fields": ('member_count', 'post_count', 'pin_count', 'view_count')}),
        ("5. 일간 통계", {"fields": ('daily_member_count', 'daily_post_count', 'daily_pin_count')}),
        ("6. 주간 통계", {"fields": ('weekly_member_count', 'weekly_post_count', 'weekly_pin_count')}),
        ("7. 월간 통계", {"fields": ('monthly_member_count', 'monthly_post_count', 'monthly_pin_count')}),
        ("8, 클럽 권한", {"fields": ('board_permission', 'merge_permission',)})
    )

    readonly_fields = ("created", "modified", 'profile_image_tag', 'banner_image_tag', 'profile_image_url', 'banner_image_url',
                       'member_count', 'post_count', 'pin_count', 'user_data',
                       'daily_member_count', 'daily_post_count', 'daily_pin_count',
                       'weekly_member_count', 'weekly_post_count', 'weekly_pin_count',
                       'monthly_member_count', 'monthly_post_count', 'monthly_pin_count',
                       )
