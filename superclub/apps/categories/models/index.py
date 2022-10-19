# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model
from superclub.apps.categories.models.mixins.club import CategoryClubMixin


class Category(Model,
               CategoryClubMixin):
    translation = models.ForeignKey('translations.Translation',
                                    verbose_name=_('번역'),
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True)
    name = models.CharField(_('이름'), max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('카테고리')
        db_table = 'categories'
        ordering = ['-club_count']

    def __str__(self):
        return self.name
