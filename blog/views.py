from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from .models import Blog, LikeBlog, BlogComment
from .serializers import BlogSerializer,\
    LikeBlogSerializer,\
    BlogCommentSerializer
from rest_framework.pagination import LimitOffsetPagination

User = get_user_model()


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = LimitOffsetPagination
    filter_fields = (
            'pet',
            'title',
            'content',
            'is_published',
            'create_user',
            'update_user')


class LikeBlogViewSet(viewsets.ModelViewSet):
    queryset = LikeBlog.objects.all().order_by('-created_at')
    serializer_class = LikeBlogSerializer
    filter_fields = ('user', 'blog')


class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all().order_by('-created_at')
    serializer_class = BlogCommentSerializer
    filter_fields = ('blog', 'content', 'created_at')
