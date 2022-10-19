# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def club_pin_decorator(title='', request_body=''):
    return dict(
        operation_id=_('클럽 핀'),
        operation_description=_(
            '## < 클럽 핀 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def club_unpin_decorator(title='', request_body=''):
    return dict(
        operation_id=_('클럽 언핀'),
        operation_description=_(
            '## < 클럽 언핀 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def post_pin_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 핀'),
        operation_description=_(
            '## < 게시글 핀 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def post_unpin_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 언핀'),
        operation_description=_(
            '## < 게시글 언핀 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )
