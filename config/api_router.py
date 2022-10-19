# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# users
from template.apps.users.api.views import UserViewSet


# Router
router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserViewSet)

app_name = 'api'
urlpatterns = [
                  path('', include("template.apps.users.urls")),
              ] + router.urls
