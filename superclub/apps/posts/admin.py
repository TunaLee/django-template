from django.contrib import admin
from django.utils.html import format_html

from superclub.apps.posts.models.index import Post, PostImage, PostVideo
from superclub.bases.admin import Admin
from superclub.bases.inlines import StackedInline


class PostImageInline(StackedInline):
    model = PostImage
    fieldsets = (
        ("이미지", {"fields": ('image',)}),
    )
    extra = 0


class PostVideoInline(StackedInline):
    model = PostVideo
    fieldsets = (
        ("비디오", {"fields": ('video',)}),
    )
    extra = 0


@admin.register(Post)
class PostAdmin(Admin):
    list_display = ('club', 'board', 'user', 'thumbnail_tag', 'title', 'is_active', 'report_count')
    search_fields = ('board__name', 'user__email', 'title')
    list_filter = ('board',)

    fieldsets = (
        ("1. 정보", {"fields": ('club', 'board', 'title', 'content', 'is_active', 'report_count')}),
        ("2. 이미지", {"fields": ('thumbnail_image', 'thumbnail_image_url')}),
        ("3. 유저", {"fields": ('user',)}),
    )

    readonly_fields = ('club', 'thumbnail_image_url',)

    inlines = (PostImageInline, PostVideoInline)

    def thumbnail_tag(self, obj):
        if obj.thumbnail_image:
            return format_html(f'<img src="{obj.thumbnail_image_url}" width="100px;"/>')



@admin.register(PostImage)
class PostImageAdmin(Admin):
    list_display = ('post', 'thumbnail_image_tag', )
    search_fields = ('post__title',)
    list_filter = ('post',)
    fieldsets = (
        ("1. 정보", {"fields": ('post',)}),
        ("2. 이미지", {"fields": ('image',)})
    )


    def thumbnail_image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.thumbnail_image_url}" width="100px;"/>')


@admin.register(PostVideo)
class PostVideoAdmin(Admin):
    list_display = ('post', 'thumbnailVideo_tag', 'view_count')
    search_fields = ('post__title',)
    list_filter = ('post',)
    ordering = ('view_count',)

    fieldsets = (
        ("1. 정보", {"fields": ('post', 'view_count')}),
        ("2. 비디오", {"fields": ('video',)})
    )

    readonly_fields = ('view_count',)

    def thumbnailVideo_tag(self, obj):
        if obj.video:
            return format_html(f'<img src="{obj.thumbnail_image_url}" width="100px;"/>')
