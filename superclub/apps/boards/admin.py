from django.contrib import admin

from superclub.apps.boards.models import Board, BoardGroup
from superclub.bases.admin import Admin
from superclub.bases.inlines import StackedInline


class BoardInline(StackedInline):
    model = Board
    fieldsets = (
        ("게시판", {"fields": ('name',)}),
    )
    extra = 0


@admin.register(BoardGroup)
class BoardGroupAdmin(Admin):
    list_display = ('club', 'name')
    search_fields = ('club__name',)
    list_filter = ('club',)

    fieldsets = (
        ("1. 정보", {"fields": ('club', 'name')}),
        ("2. 활성화 여부", {"fields": ('is_active',)}),
    )
    add_fieldsets = (
        ("1. 정보", {"fields": ('club', 'name')}),
        ("2. 활성화 여부", {"fields": ('is_active',)}),
    )

    inlines = (BoardInline,)


@admin.register(Board)
class BoardAdmin(Admin):
    list_display = ('club', 'board_group', 'name', 'is_active')
    search_fields = ('board_group__name',)
    list_filter = ('board_group',)

    fieldsets = (
        ("1. 정보", {"fields": ('club', 'board_group', 'name',)}),
        ("2. 활성화 여부", {"fields": ('is_active',)}),
        ("3. 게시판 권한",
         {"fields": ('merge_permission', 'write_permission', 'read_permission')}),
    )
    add_fieldsets = (
        ("1. 정보", {"fields": ('club', 'board_group', 'name',)}),
        ("2. 활성화 여부", {"fields": ('is_active',)}),
        ("3. 게시판 권한",
         {"fields": ('merge_permission', 'write_permission', 'read_permission')})
    )
    readonly_fields = ()


