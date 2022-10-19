# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# categories
from superclub.apps.categories.api.views.index import CategoriesViewSet

# clubs
from superclub.apps.clubs.api.views.index import ClubViewSet, ClubsViewSet, ClubAdminViewSet, ClubsAdminViewSet

# comments
from superclub.apps.comments.api.views.index import CommentsViewSet, CommentViewSet

# boards
from superclub.apps.boards.api.views.index import BoardGroupViewSet, BoardViewSet, BoardGroupAdminViewSet, \
    BoardAdminViewSet
from superclub.apps.boards.api.views.club_board_groups import ClubBoardGroupsViewSet
from superclub.apps.likes.api.views.index import PostLikesViewSet

# posts
from superclub.apps.posts.api.views.index import PostViewSet, PostsViewSet, PostsAdminViewSet, PostAdminViewSet
from superclub.apps.posts.api.views.board_post import BoardPostsViewSet
from superclub.apps.posts.api.views.club_post import ClubPostsViewSet

# profiles
from superclub.apps.profiles.api.views.club_profile import ClubProfilesViewSet
from superclub.apps.profiles.api.views.index import ProfileViewSet

# tags
from superclub.apps.tags.api.views.index import TagsViewSet

# users
from superclub.apps.users.api.views import UserViewSet


# Router
router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserViewSet)
router.register("categories", CategoriesViewSet)
router.register("clubs", ClubsViewSet)
router.register("board-group", BoardGroupViewSet)
router.register("posts", PostsViewSet)
router.register("profile", ProfileViewSet)
router.register("comment", CommentViewSet)
router.register("tags", TagsViewSet)

router.register("admin/club", ClubAdminViewSet)
router.register("admin/clubs", ClubsAdminViewSet)
router.register("admin/board-group", BoardGroupAdminViewSet)
router.register("admin/board", BoardAdminViewSet)
router.register("admin/posts", PostsAdminViewSet)

# Club Nested Router
router.register(r"club", ClubViewSet, basename='club')
club_profiles_router = routers.NestedSimpleRouter(router, r"club", lookup="club")
club_profiles_router.register(r'profiles', ClubProfilesViewSet, basename='club-profiles')
club_board_groups_router = routers.NestedSimpleRouter(router, r"club", lookup="club")
club_board_groups_router.register(r'board-groups', ClubBoardGroupsViewSet, basename='club-board-groups')
club_posts_router = routers.NestedSimpleRouter(router, r"club", lookup="club")
club_posts_router.register(r'posts', ClubPostsViewSet, basename='club-posts')

# Board Nested Router
router.register(r"board", BoardViewSet, basename='board')
board_posts_router = routers.NestedSimpleRouter(router, r"board", lookup="board")
board_posts_router.register(r'posts', BoardPostsViewSet, basename='board-posts')

# Post Nested Router
router.register(r"post", PostViewSet, basename='post')
router.register(r"admin/post", PostAdminViewSet, basename='admin/post')
post_comments_router = routers.NestedSimpleRouter(router, r"post", lookup="post")
post_comments_router.register(r'comments', CommentsViewSet, basename='post-comments')
post_likes_router = routers.NestedSimpleRouter(router, r"post", lookup="post")
post_likes_router.register(r'likes', PostLikesViewSet, basename='post-likes')

app_name = 'api'
urlpatterns = [
                  path('', include("superclub.apps.users.urls")),
                  path("", include(club_profiles_router.urls)),
                  path("", include(club_board_groups_router.urls)),
                  path("", include(club_posts_router.urls)),
                  path("", include(board_posts_router.urls)),
                  path("", include(post_comments_router.urls)),
                  path("", include(post_likes_router.urls))
              ] + router.urls
