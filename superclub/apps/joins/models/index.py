# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Managers
from superclub.apps.joins.models.managers.active import JoinActiveManager
from superclub.apps.joins.models.managers.objects import JoinMainManager

# Models
from superclub.bases.models import Model


# Class Section
class Join(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='joins')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='joins')
    club_data = models.JSONField(_('클럽 데이터'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('조인')
        db_table = 'joins'
        unique_together = ('club', 'user')
        ordering = ['-created']

    objects = JoinMainManager()
    active = JoinActiveManager()

    def save(self, *args, **kwargs):
        super(Join, self).save(*args, **kwargs)

        self.club.update_member_count()
        self.club.update_daily_member_count()
        self.club.save()

        self.user.update_user_join_count()
        self.user.save()
