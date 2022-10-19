# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def post_like_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 좋아요'),
        operation_description=_(
            '## < 게시글 좋아요 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def post_unlike_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 좋아요 취소'),
        operation_description=_(
            '## < 게시글 좋아요 취소 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def post_dislike_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 싫어요'),
        operation_description=_(
            '## < 게시글 싫어요 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def post_undislike_decorator(title='', request_body=''):
    return dict(
        operation_id=_('게시글 싫어요 취소'),
        operation_description=_(
            '## < 게시글 싫어요 취소 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def post_like_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('게시글 좋아요 리스트 조회'),
        operation_description=_(
            '## < 게시글 좋아요 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )


def comment_like_decorator(title='', request_body=''):
    return dict(
        operation_id=_('댓글 좋아요'),
        operation_description=_(
            '## < 댓글 좋아요 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def comment_unlike_decorator(title='', request_body=''):
    return dict(
        operation_id=_('댓글 좋아요 취소'),
        operation_description=_(
            '## < 댓글 좋아요 취소 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def comment_dislike_decorator(title='', request_body=''):
    return dict(
        operation_id=_('댓글 싫어요'),
        operation_description=_(
            '## < 댓글 싫어요 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )


def comment_undislike_decorator(title='', request_body=''):
    return dict(
        operation_id=_('댓글 싫어요 취소'),
        operation_description=_(
            '## < 댓글 싫어요 취소 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )
