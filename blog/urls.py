from django.urls import include, path
from rest_framework import routers
from .views import BlogViewSet, LikeBlogViewSet, BlogCommentViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'like_blog', LikeBlogViewSet)
router.register(r'blog_comment', BlogCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
