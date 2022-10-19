# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class CommentLikeModelMixin(models.Model):
    like_count = models.IntegerField(_('좋아요 수'), default=0)
    dislike_count = models.IntegerField(_('싫어요 수'), default=0)

    class Meta:
        abstract = True

    def update_comment_like_count(self):
        self.like_count = self.comment_likes.filter(is_active=True).count()

    def update_comment_dislike_count(self):
        self.dislike_count = self.comment_dislikes.filter(is_active=True).count()
