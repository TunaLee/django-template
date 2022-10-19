# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def post_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('게시글 리스트 조회'),
        operation_description=_(
            '## < 게시글 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def post_view_count_decorator(title='', serializer=None):
    return dict(
        operation_id=_('게시글 조회수 조회'),
        operation_description=_(
            '## < 게시글 조회수 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def club_post_temporary_destroy_decorator(title=''):
    return dict(
        operation_id=_('임시글 일괄 삭제'),
        operation_description=_(
            '## < 임시글 일괄 삭제 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute'
        ),
        responses={204: openapi.Response(_('no content'))},
        tags=[_(f'{title}')]
    )


def post_temporary_destroy_decorator(title=''):
    return dict(
        operation_id=_('임시글 객체 삭제'),
        operation_description=_(
            '## < 임시글 객체 삭제 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute'
        ),
        responses={204: openapi.Response(_('no content'))},
        tags=[_(f'{title}')]
    )


def post_activate_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시글 활성화'),
        operation_description=_(
            '## < 게시글 활성화 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')],
    )


def posts_activate_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시글 리스트 활성화'),
        operation_description=_(
            '## < 게시글 리스트 활성화 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력(리스트 입력) \n'
            '### 3. Execute'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')],
    )


def post_deactivate_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시글 비활성화'),
        operation_description=_(
            '## < 게시글 비활성화 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')],
    )


def posts_deactivate_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시글 리스트 비활성화'),
        operation_description=_(
            '## < 게시글 리스트 비활성화 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력(리스트 입력) \n'
            '### 3. Execute'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')],
    )


def post_admin_decorator(title='', serializer=None):
    return dict(
        operation_id=_('게시글 관리자 리스트 조회'),
        operation_description=_(
            '## < 게시글 Admin 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )
