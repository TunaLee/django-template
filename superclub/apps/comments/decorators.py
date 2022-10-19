# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def post_comment_create_decorator(title='', request_body=None):
    return dict(
        operation_id=_('댓글 생성'),
        operation_description=_(
            '## < 댓글 생성 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. parameter 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def post_comment_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('댓글 리스트 조회'),
        operation_description=_(
            '## < 댓글 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )
