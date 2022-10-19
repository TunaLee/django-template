# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

from superclub.apps.reports.api.serializers.create import CommentReportCreateSerializer
# Serializers
from superclub.apps.reports.api.serializers.list import CommentReportListSerializer

# Decorators
from superclub.apps.reports.decorators import comment_report_decorator

# Utils
from superclub.utils.api.response import Response


# Class Section
class CommentReportViewMixin:
    @swagger_auto_schema(**comment_report_decorator(title='9. 댓글 - Member', request_body=CommentReportCreateSerializer))
    @action(detail=True, methods=['post'], url_path='report', url_name='comment_report')
    def comment_report(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        club = comment.club
        profile = club.profiles.filter(user=user).first()
        data = request.data
        instance = user.report_comment(comment, profile, **data)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=CommentReportListSerializer(instance=instance).data
        )
