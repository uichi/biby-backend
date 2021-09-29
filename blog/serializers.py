from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Blog, LikeBlog, BlogComment
from pet.models import Pet
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogSerializer(ModelSerializer):
    create_user_pk = PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='create_user'
    )
    update_user_pk = PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='update_user', required=False
    )
    pet_pk = PrimaryKeyRelatedField(
        queryset=Pet.objects.all(), source='pet'
    )

    class Meta:
        model = Blog
        fields = (
            'id',
            'pet',
            'pet_pk',
            'title',
            'content',
            'image',
            'is_published',
            'publish_date_time',
            'create_user_pk',
            'update_user_pk',)
        depth = 1


class LikeBlogSerializer(ModelSerializer):
    user_pk = PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user'
    )
    blog_pk = PrimaryKeyRelatedField(
        queryset=Blog.objects.all(), source='blog'
    )

    class Meta:
        model = LikeBlog
        fields = ('id', 'user_pk', 'blog_pk')
        depth = 1


class BlogCommentSerializer(ModelSerializer):
    blog_pk = PrimaryKeyRelatedField(
        queryset=Blog.objects.all(), source='blog'
    )

    class Meta:
        model = BlogComment
        fields = ('blog_pk', 'content')
