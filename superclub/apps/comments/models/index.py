# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Mixins
from superclub.apps.comments.models.mixins.like import CommentLikeModelMixin
from superclub.apps.comments.models.mixins.image import ImageModelMixin
from superclub.apps.comments.models.mixins.report import CommentReportModelMixin

# Models
from superclub.bases.models import Model


# TODO Comment Image, Post Thumbnail Image 삽입 이슈 해결하기
# Class Section
class Comment(Model,
              CommentLikeModelMixin,
              ImageModelMixin,
              CommentReportModelMixin):
    parent_comment = models.ForeignKey('self', verbose_name=_('부모 댓글'), on_delete=models.SET_NULL, null=True,
                                       related_name='comments')
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.SET_NULL, null=True,
                             related_name='comments')
    post = models.ForeignKey('posts.Post', verbose_name=_('포스트'), on_delete=models.SET_NULL, null=True,
                             related_name='comments')
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True,
                             related_name='comments')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('프로필'), on_delete=models.SET_NULL, null=True,
                                related_name='comments')
    profile_data = models.JSONField(_('프로필 데이터'), null=True, blank=True)
    child_comment_data = models.JSONField(_('자식 댓글 데이터'), null=True, blank=True)
    content = models.CharField(_('내용'), max_length=2000)
    is_secret = models.BooleanField(_('비밀 댓글 여부'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _('댓글')
        db_table = 'comments'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

        # Post Comment Count
        self.post.update_post_comment_count()
        self.post.save()

        # User Comment Count
        self.user.update_user_comment_count()
        self.user.save()

        # TODO 로직 구현하기
        # club_profile = self.user.profiles.filter(club=self.club)[0]
        # club_profile.update_profile_comment_count()
        # club_profile.save()
