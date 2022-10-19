# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class TagClubModelMixin(models.Model):
    club_count = models.IntegerField(_('클럽 수'), default=0)

    class Meta:
        abstract = True

    def update_tag_club_count(self):
        self.club_count = self.club_tags.filter(is_active=True).count()
