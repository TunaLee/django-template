# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


# Class Section
def post_report_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 신고'),
        operation_description=_(
            '## < 게시글 신고 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. `id` 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def comment_report_decorator(title='', request_body=''):
    return dict(
        operation_id=_('댓글 신고'),
        operation_description=_(
            '## < 댓글 신고 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. `id` 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )
