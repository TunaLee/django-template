# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def club_thumbnail_image_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('썸네일 이미지 수정'),
        operation_description=_(
            '## < 썸네일 이미지 수정 API 입니다. > \n'
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


def club_profile_image_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('프로필 이미지 수정'),
        operation_description=_(
            '## < 프로필 이미지 수정 API 입니다. > \n'
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


def club_banner_image_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('배너 이미지 수정'),
        operation_description=_(
            '## < 배너 이미지 수정 API 입니다. > \n'
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


def club_check_name_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('클럽 이름 유효성 검사(수정)'),
        operation_description=_(
            '## < 클럽 이름 유효성 검사 API 입니다. > \n'
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


def club_check_address_update_decorator(title='', request_body=None):
    return dict(
        operation_id=_('클럽 주소 유효성 검사(수정)'),
        operation_description=_(
            '## < 클럽 주소 유효성 검사 API 입니다. > \n'
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


def club_check_name_create_decorator(title='', request_body=None):
    return dict(
        operation_id=_('클럽 이름 유효성 검사(생성)'),
        operation_description=_(
            '## < 클럽 이름 유효성 검사 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `name` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def club_check_address_create_decorator(title='', request_body=None):
    return dict(
        operation_id=_('클럽 주소 유효성 검사(생성)'),
        operation_description=_(
            '## < 클럽 주소 유효성 검사 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `address` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def club_dashboard_decorator(title='', serializer=None):
    return dict(
        operation_id=_('클럽 대시보드 조회'),
        operation_description=_(
            '## < 클럽 대시보드 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def club_post_create_decorator(title='', request_body=None):
    return dict(
        operation_id=_('게시글 생성'),
        operation_description=_(
            '## < 게시글 생성 API 입니다. > \n'
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
