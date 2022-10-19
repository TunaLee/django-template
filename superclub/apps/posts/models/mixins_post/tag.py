# Django
from django.db import models
from django.db.models import Q

# Models
from superclub.apps.tags.models.index import Tag
from superclub.apps.post_tags.models.index import PostTag


# Class Section
class PostTagModelMixin(models.Model):
    class Meta:
        abstract = True

    def set_post_tag(self, index, tag):
        tag, created = Tag.objects.get_or_create(name=tag.lower().replace(' ', ''))
        post_tag, created = PostTag.objects.get_or_create(post=self, tag=tag)
        post_tag.update(order=index, name=tag.name)

    def update_post_tag(self, tags):
        PostTag.objects.filter(post=self).filter(~Q(tag__name__in=tags)).delete()
        for index, tag in enumerate(tags):
            tag, created = Tag.objects.get_or_create(name=tag.lower().replace(' ', ''))
            if created:
                print('[Post] update_post_tag', tag, '생성')
            post_tag, created = PostTag.objects.get_or_create(post=self, tag=tag)
            post_tag.update(order=index, name=tag.name)
