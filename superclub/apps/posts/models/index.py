# Python
import os
from time import strftime, gmtime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Managers
from superclub.apps.posts.models.managers.active import PostActiveManager
from superclub.apps.posts.models.managers.objects import PostMainManager
from superclub.apps.posts.models.mixins_post.pin import PostPinModelMixin

# Bases
from superclub.bases.models import Model

# Mixins
from superclub.apps.posts.models.mixins_post.comment import PostCommentModelMixin
from superclub.apps.posts.models.mixins_post.image import PostImageModelMixin
from superclub.apps.posts.models.mixins_post.like import PostLikeModelMixin
from superclub.apps.posts.models.mixins_post.share import PostShareModelMixin
from superclub.apps.posts.models.mixins_post.view import PostViewModelMixin
from superclub.apps.posts.models.mixins_post.tag import PostTagModelMixin
from superclub.apps.posts.models.mixins_post_video.view import PostVideoViewModelMixin
from superclub.apps.posts.models.mixins_post.report import PostReportModelMixin


# Class Section
class Post(Model,
           PostCommentModelMixin,
           PostImageModelMixin,
           PostLikeModelMixin,
           PostShareModelMixin,
           PostViewModelMixin,
           PostPinModelMixin,
           PostTagModelMixin,
           PostReportModelMixin):
    # Club
    club = models.ForeignKey('clubs.Club', verbose_name=_('클럽'), on_delete=models.PROTECT, related_name='posts',
                             null=True)
    club_name = models.CharField(_('클럽 이름'), max_length=60, null=True, blank=True)
    # Board Group
    board_group = models.ForeignKey('boards.BoardGroup', verbose_name=_('게시판 그룹'), on_delete=models.SET_NULL, null=True,
                                    related_name='posts')
    board_group_name = models.CharField(_('게시판 그룹 이름'), max_length=60, null=True, blank=True)

    # Board
    board = models.ForeignKey('boards.Board', verbose_name=_('게시판'), on_delete=models.SET_NULL, null=True,
                              related_name='posts')
    board_name = models.CharField(_('게시판 이름'), max_length=60, null=True, blank=True)
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.SET_NULL, null=True,
                             related_name='posts')
    user_email = models.CharField(_('유저 이메일'), max_length=60, null=True, blank=True)
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('프로필'), on_delete=models.SET_NULL, null=True,
                                related_name='posts')
    profile_data = models.JSONField(_('프로필 데이터'), null=True, blank=True)
    title = models.CharField(_('제목'), max_length=100, default='Untitled')
    content = models.TextField(_('내용'), null=True, blank=True)
    popularity = models.IntegerField(_('인기'), default=0)

    is_video = models.BooleanField(_('비디오 게시글 여부'), default=False)
    is_image = models.BooleanField(_('이미지 게시글 여부'), default=False)
    is_temporary = models.BooleanField(_('임시글 여부'), default=False)
    is_secret = models.BooleanField(_('비밀글 여부'), default=False)
    password = models.IntegerField(_('비밀번호'), null=True, blank=True)
    is_notice = models.BooleanField(_('공지 여부'), default=False)
    is_event = models.BooleanField(_('이벤트 여부'), default=False)
    is_comment = models.BooleanField(_('댓글 여부'), default=True)
    is_share = models.BooleanField(_('공유 여부'), default=True)
    is_search = models.BooleanField(_('검색 여부'), default=True)

    objects = PostMainManager()
    active = PostActiveManager()

    class Meta:
        verbose_name = verbose_name_plural = _('포스트')
        db_table = 'posts'
        ordering = ['-created']

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        self.club.update_post_count()
        self.club.update_daily_post_count()
        self.club.save()

        # TODO 로직 완성하기
        # self.user.update_user_post_count()
        # self.user.save()

        # club_profile = self.user.profiles.filter(club=self.club)[0]
        # club_profile.update_profile_post_count()
        # club_profile.save()


class PostImage(Model):

    def image_path(instance, filename):
        upload_to = 'Post/DetailImage/'
        time = strftime("%Y%m%dT%H%M%S", gmtime())
        ext = filename.split('.')[-1]
        filename = f'{time}.{ext}'
        return os.path.join(upload_to, filename)

    post = models.ForeignKey('Post', verbose_name=_('포스트'), on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(_('이미지'), upload_to=image_path)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)
    thumbnail_image = models.ImageField(_('썸네일 이미지'), null=True, blank=True)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('포스트 이미지')
        db_table = 'post_images'
        ordering = ['-created']

    def __str__(self):
        return self.id


class PostVideo(Model,
                PostVideoViewModelMixin):
    post = models.ForeignKey('Post', verbose_name=_('포스트'), on_delete=models.CASCADE, related_name='post_videos')
    video = models.FileField(_('비디오'))
    video_url = models.URLField(_('비디오 URL'), null=True, blank=True)
    thumbnail_image = models.ImageField(_('썸네일 이미지'), null=True, blank=True)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('포스트 비디오')
        db_table = 'post_videos'
        ordering = ['-created']

    def __str__(self):
        return f'{self.post}'
