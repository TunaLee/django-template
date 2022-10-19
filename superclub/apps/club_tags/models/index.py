# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model


class ClubTag(Model):
    tag = models.ForeignKey('tags.Tag', verbose_name=_('태그'), on_delete=models.CASCADE, related_name='club_tags')
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='club_tags')
    name = models.CharField(_('태그 이름'), max_length=100, null=True, blank=True)
    order = models.IntegerField(_('순서'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('클럽 태그')
        db_table = 'club_tags'

    def save(self, *args, **kwargs):
        super(ClubTag, self).save(*args, **kwargs)

        self.tag.update_tag_club_count()
        self.tag.save()
