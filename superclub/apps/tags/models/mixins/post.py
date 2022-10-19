# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class TagPostModelMixin(models.Model):
    post_count = models.IntegerField(_('포스트 수'), default=0)

    class Meta:
        abstract = True

    def update_tag_post_count(self):
        self.post_count = self.post_tags.filter(is_active=True, post__is_temporary=False).count()
