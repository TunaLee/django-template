from django.contrib import admin

from superclub.apps.pins.models.index import ClubPin
from superclub.bases.admin import CountAdmin


@admin.register(ClubPin)
class ClubPinAdmin(CountAdmin):
    list_display = ('club', 'user')
    search_fields = ('club__name', 'user__email')
    readonly_fields = ('club', 'user')

