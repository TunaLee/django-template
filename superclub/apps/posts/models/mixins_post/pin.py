# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class PostPinModelMixin(models.Model):
    pin_count = models.IntegerField(_('핀 수'), default=0)

    class Meta:
        abstract = True

    def update_post_pin_count(self):
        self.pin_count = self.post_pins.filter(is_active=True).count()
