# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Manager
from superclub.apps.likes.models.managers.active import PostLikeActiveManager
from superclub.apps.likes.models.managers.objects import PostLikeMainManager

# Models
from superclub.bases.models import Model


class CommentLike(Model):
    comment = models.ForeignKey('comments.Comment', verbose_name=_('댓글'), on_delete=models.SET_NULL, null=True, related_name='comment_likes')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True, related_name='comment_likes')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('프로필'), on_delete=models.SET_NULL, null=True, related_name='comment_likes')

    class Meta:
        verbose_name = verbose_name_plural = _('댓글 좋아요')
        db_table = 'comment_likes'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(CommentLike, self).save(*args, **kwargs)

        self.comment.update_comment_like_count()
        self.comment.save()


class CommentDislike(Model):
    comment = models.ForeignKey('comments.Comment', verbose_name=_('댓글'), on_delete=models.SET_NULL, null=True, related_name='comment_dislikes')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True, related_name='comment_dislikes')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('프로필'), on_delete=models.SET_NULL, null=True, related_name='comment_dislikes')

    class Meta:
        verbose_name = verbose_name_plural = _('댓글 싫어요')
        db_table = 'comment_dislikes'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(CommentDislike, self).save(*args, **kwargs)

        self.comment.update_comment_dislike_count()
        self.comment.save()


class PostLike(Model):
    post = models.ForeignKey('posts.Post', verbose_name=_('포스트'), on_delete=models.SET_NULL, null=True, related_name='post_likes')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True, related_name='post_likes')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('프로필'), on_delete=models.SET_NULL, null=True, related_name='post_likes')
    profile_data = models.JSONField(_('프로필 데이터'), null=True, blank=True)

    objects = PostLikeMainManager()
    active = PostLikeActiveManager()

    class Meta:
        verbose_name = verbose_name_plural = _('포스트 좋아요')
        db_table = 'post_likes'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(PostLike, self).save(*args, **kwargs)

        self.post.update_post_like_count()
        self.post.save()


class PostDislike(Model):
    post = models.ForeignKey('posts.Post', verbose_name=_('포스트'), on_delete=models.SET_NULL, null=True, related_name='post_dislikes')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True, related_name='post_dislikes')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('프로필'), on_delete=models.SET_NULL, null=True, related_name='post_dislikes')
    profile_data = models.JSONField(_('프로필 데이터'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('포스트 싫어요')
        db_table = 'post_dislikes'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(PostDislike, self).save(*args, **kwargs)

        self.post.update_post_dislike_count()
        self.post.save()
