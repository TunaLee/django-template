# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Modules
from superclub.modules.choices import LINK_SHARE_CHOICES

# Models
from superclub.bases.models import Model


class ClubShare(Model):
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='club_shares')
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='club_shares')
    link = models.CharField(_('링크'), choices=LINK_SHARE_CHOICES, max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('클럽 공유')
        db_table = 'club_shares'
        ordering = ['-created']


class PostShare(Model):
    post = models.ForeignKey('posts.Post', verbose_name=_('포스트'), on_delete=models.CASCADE, related_name='post_shares')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='post_shares')
    link = models.CharField(_('링크'), choices=LINK_SHARE_CHOICES, max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _('포스트 공유')
        db_table = 'post_shares'
        ordering = ['-created']
