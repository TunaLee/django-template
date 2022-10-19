from django.contrib import admin
from superclub.apps.categories.models.index import Category
from superclub.bases.admin import Admin


@admin.register(Category)
class CategoryAdmin(Admin):
    list_display = ('translation', 'name', 'club_count')
    search_fields = ('translation__ko', 'translation__en', 'translation__ja', 'translation__zh', 'name', 'club_count')
    # list_filter = (('club_count', SliderNumericFilter),
    #                'translation')

    ordering = ('created',)

    fieldsets = (
        ("1. 번역", {"fields": ('translation',)}),
        ("2. 정보", {"fields": ('name', 'club_count')}),
    )

    add_fieldsets = (
        ("1. 번역", {"fields": ('translation',)}),
        ("2. 정보", {"fields": ('name', 'club_count')}),
    )

    readonly_fields = ("created", "modified", 'club_count')
