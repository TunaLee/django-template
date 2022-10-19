from django.contrib import admin

from superclub.apps.translations.models.index import Translation
from superclub.bases.admin import Admin


@admin.register(Translation)
class TranslationAdmin(Admin):
    list_display = ('ko', 'en', 'ja', 'zh')
    search_fields = ('ko', 'en', 'ja', 'zh')

    fieldsets = (
        ("한국어", {"fields": ('ko',)}),
        ("영어", {"fields": ('en',)}),
        ("일본어", {"fields": ('ja',)}),
        ("중국어", {"fields": ('zh',)}),
    )




