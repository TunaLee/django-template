# Django
from django.db import models

# Local
from superclub.apps.boards.models import BoardGroup


class ClubBoardGroupModelMixin(models.Model):
    class Meta:
        abstract = True

    def board_group_club(self, name, is_active):
        return BoardGroup.objects.create(club=self, name=name, is_active=is_active)
