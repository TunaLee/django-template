# Django
from django.db import models
from django.db.models import Q

# Local
from superclub.apps.club_tags.models.index import ClubTag
from superclub.apps.tags.models.index import Tag


class ClubTagModelMixin(models.Model):
    class Meta:
        abstract = True

    def set_club_tag(self, index, tag):
        tag, created = Tag.objects.get_or_create(name=tag.lower().replace(' ', ''))
        club_tag, created = ClubTag.objects.get_or_create(club=self, tag=tag)
        club_tag.update(order=index, name=tag.name)

    def update_club_tag(self, tags):
        ClubTag.objects.filter(club=self).filter(~Q(tag__name__in=tags)).delete()
        for index, tag in enumerate(tags):
            tag, created = Tag.objects.get_or_create(name=tag.lower().replace(' ', ''))
            if created:
                print('[Club] update_club_tag', tag, '생성')
            club_tag, created = ClubTag.objects.get_or_create(club=self, tag=tag)
            club_tag.update(order=index, name=tag.name)
