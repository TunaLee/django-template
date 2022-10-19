# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model

# Modules
from superclub.modules.choices import REPORT_TYPE_CHOICES


# Class Section
class PostReport(Model):
    post = models.ForeignKey('posts.Post',
                             verbose_name=_('게시글'),
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='post_reports')
    user = models.ForeignKey('users.User', verbose_name=_('유저'),
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='post_reports')
    profile = models.ForeignKey('profiles.Profile',
                                verbose_name=_('프로필'),
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='post_reports')
    profile_data = models.JSONField(_('프로필 데이터'), null=True, blank=True)
    type = models.CharField(_('타입'), choices=REPORT_TYPE_CHOICES, max_length=100)
    content = models.CharField(_('내용'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('게시글 신고')
        db_table = 'post_reports'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(PostReport, self).save(*args, **kwargs)

        self.post.update_post_report_count()
        self.post.report_date = self.created
        self.post.save()


class CommentReport(Model):
    comment = models.ForeignKey('comments.Comment',
                                verbose_name=_('댓글'),
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='comment_reports')
    user = models.ForeignKey('users.User',
                             verbose_name=_('유저'),
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='comment_reports')
    profile = models.ForeignKey('profiles.Profile',
                                verbose_name=_('프로필'),
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='comment_reports')
    profile_data = models.JSONField(_('프로필 데이터'), null=True, blank=True)
    type = models.CharField(_('타입'), choices=REPORT_TYPE_CHOICES, max_length=100)
    content = models.CharField(_('내용'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('댓글 신고')
        db_table = 'comment_reports'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(CommentReport, self).save(*args, **kwargs)

        self.comment.update_comment_report_count()
        self.comment.report_date = self.created
        self.comment.save()

