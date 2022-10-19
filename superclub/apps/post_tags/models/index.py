# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from superclub.bases.models import Model


class PostTag(Model):
    tag = models.ForeignKey('tags.Tag', verbose_name=_('태그'), on_delete=models.CASCADE, related_name='post_tags')
    post = models.ForeignKey('posts.Post', verbose_name=_('게시글'), on_delete=models.CASCADE, related_name='post_tags')
    name = models.JSONField(_('태그 이름'), null=True, blank=True)
    order = models.IntegerField(_('순서'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('게시글 태그')
        db_table = 'post_tags'

    def save(self, *args, **kwargs):
        super(PostTag, self).save(*args, **kwargs)

        self.tag.update_tag_post_count()
        self.tag.save()
