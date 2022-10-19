# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model


class ClubView(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='club_views')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='club_views')

    class Meta:
        verbose_name = verbose_name_plural = _('클럽 조회수')
        db_table = 'club_views'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.club.update_view_count()
        self.club.update_daily_view_count()
        self.club.save()
        return super(ClubView, self).save(*args, **kwargs)


class PostView(Model):
    post = models.ForeignKey('posts.Post', verbose_name=_('포스트'), on_delete=models.CASCADE, related_name='post_views')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='post_views')

    class Meta:
        verbose_name = verbose_name_plural = _('게시글 조회수')
        db_table = 'post_views'
        ordering = ['-created']


class PostVideoView(Model):
    post_video = models.ForeignKey('posts.PostVideo', verbose_name=_('포스트 비디오'), on_delete=models.CASCADE,
                                  related_name='post_video_views')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE,
                             related_name='post_video_views')

    class Meta:
        verbose_name = verbose_name_plural = _('포스트 비디오 조회수')
        db_table = 'post_video_views'
        ordering = ['-created']
