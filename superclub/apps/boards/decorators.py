# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def club_board_group_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('게시판 그룹 리스트 조회'),
        operation_description=_(
            '## < 게시판 그룹 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def club_board_group_create_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 그룹 생성'),
        operation_description=_(
            '## < 게시판 그룹 생성 API 입니다. > \n'
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


def board_group_board_create_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 생성'),
        operation_description=_(
            '## < 게시판 생성 API 입니다. > \n'
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


def board_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('게시판 리스트 조회'),
        operation_description=_(
            '## < 게시판 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def board_group_order_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 그룹 순서 변경'),
        operation_description=_(
            '## < 게시판 그룹 순서 변경 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. parameter 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def board_order_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 순서 변경'),
        operation_description=_(
            '## < 게시판 순서 수정 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. parameter 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def board_group_merge_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 그룹 병합'),
        operation_description=_(
            '## < 게시판 그룹 병합 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. parameter 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def board_merge_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 병합'),
        operation_description=_(
            '## < 게시판 병합 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. parameter 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def board_destroy_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시판 삭제'),
        operation_description=_(
            '## < 게시판 삭제 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. parameter 입력 \n'
            '### 4. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )
