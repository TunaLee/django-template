# Django
from django.conf import settings
from django.urls import include, path
from django.utils.translation import ugettext_lazy as _

# Django Rest Framework
from rest_framework import permissions

# Third party
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

description = _(
    """
API 문서입니다.

# Response Data
<br/>
## 성공
```json
{
    "code": " ... ",
    "message": " ... ",
    "data": { ... }
}
```
<br/>
## 실패
```json
{
    "code": " ... ",
    "message": " ... ",
    "errors": { ... },
}
```
<br/>
## 세부 안내

`code` Status 코드입니다.

`message` 상세 메시지입니다.

`data` 응답 결과 데이터입니다.

`errors` 오류 발생시 나타나는 필드입니다.

<br/>"""
)

# Only expose to public in local and development.
public = bool(settings.DJANGO_ENV in ('local',))

# Fully exposed to only for local, else at least should be staff.
if settings.DJANGO_ENV == "local":
    permission_classes = (permissions.AllowAny,)
else:
    permission_classes = (permissions.IsAdminUser,)

schema_url_patterns = [
    path(r"^api/v1/", include("config.api_router")),
]

schema_view = get_schema_view(
    openapi.Info(
        title=_("API 문서"),
        default_version="v1",
        description=description,
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Copyright 2022. Daniel Lee. all rights reserved."),
    ),
    public=public,
    permission_classes=permission_classes,
    patterns=schema_url_patterns,
)
