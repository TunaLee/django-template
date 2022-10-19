# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProfileVisitModelMixin(models.Model):
    visit_count = models.IntegerField(_('방문 수'), default=0)

    class Meta:
        abstract = True
