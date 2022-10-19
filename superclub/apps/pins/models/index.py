# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model


class ClubPin(Model):
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.CASCADE, related_name='club_pins')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='club_pins')

    class Meta:
        verbose_name = verbose_name_plural = _('핀')
        db_table = 'club_pins'
        unique_together = ('club', 'user')
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(ClubPin, self).save(*args, **kwargs)

        # Club Pin Count
        self.club.update_club_pin_count()
        self.club.save()

        # User Club Pin Count
        self.user.update_user_club_pin_count()
        self.user.save()


class PostPin(Model):
    post = models.ForeignKey('posts.Post', verbose_name=_('게시글'), on_delete=models.CASCADE, related_name='post_pins')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='post_pins')

    class Meta:
        verbose_name = verbose_name_plural = _('핀')
        db_table = 'post_pins'
        unique_together = ('post', 'user')
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(PostPin, self).save(*args, **kwargs)

        # Post Pin Count
        self.post.update_post_pin_count()
        self.post.save()

        # User Club Pin Count
        self.user.update_user_post_pin_count()
        self.user.save()
