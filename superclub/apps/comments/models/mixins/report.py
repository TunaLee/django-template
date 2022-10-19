# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class CommentReportModelMixin(models.Model):
    report_count = models.IntegerField(_('신고 수'), default=0)
    report_date = models.DateTimeField(_('최근 신고 날짜'), null=True, blank=True)

    class Meta:
        abstract = True

    def update_comment_report_count(self):
        self.report_count = self.comment_reports.filter(is_active=True).count()
