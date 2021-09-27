from rest_framework.serializers import ModelSerializer, CharField, PrimaryKeyRelatedField
from .models import Blog, LikeBlog, BlogComment
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'pet',
            'title',
            'content',
            'image',
            'is_published',
            'publish_datetime',
            'update_user',)


class LikeBlogSerializer(ModelSerializer):
    user_pk = PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    blog_pk = PrimaryKeyRelatedField(
        queryset=Blog.objects.all(), source='blog'
    )

    class Meta:
        model = LikeBlog
        fields = ('user_pk', 'blog_pk')
        depth = 1


class BlogCommentSerializer(ModelSerializer):
    blog_pk = PrimaryKeyRelatedField(
        queryset=Blog.objects.all(), source='blog'
    )

    class Meta:
        model = BlogComment
        fields = ('blog_pk', 'content')
