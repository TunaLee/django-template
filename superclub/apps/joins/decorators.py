# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def club_join_decorator(title='', request_body=None):
    return dict(
        operation_id=_('클럽 조인'),
        operation_description=_(
            '## < 클럽 조인 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def club_leave_decorator(title='', request_body=''):
    return dict(
        operation_id=_('클럽 탈퇴'),
        operation_description=_(
            '## < 클럽 탈퇴 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )
