from django.db.models import BooleanField, \
    CharField, \
    DateTimeField, \
    ForeignKey, \
    TextField, \
    BooleanField
from django.db.models import CASCADE, SET_NULL, Model, ManyToManyField, UniqueConstraint
from pet.models import Pet
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField

User = get_user_model()


# Blog
class Blog(Model):
    pet = ForeignKey(Pet, on_delete=CASCADE, null=False)
    title = CharField(max_length=256, blank=True, null=True)
    content = TextField(blank=True, null=True)
    image = ProcessedImageField(upload_to='blog_images',
                                options={'quality': 100},
                                blank=True,
                                null=True)
    is_published = BooleanField(blank=True, null=False, default=False)
    publish_date_time = DateTimeField(blank=True, null=True)
    create_user = ForeignKey(User, on_delete=SET_NULL, blank=False, null=True, related_name='create_user')
    update_user = ForeignKey(User, on_delete=SET_NULL, blank=True, null=True, related_name='update_user')
    likes = ManyToManyField(
        User,
        through='LikeBlog',
        blank=True
    )
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    def __str__(self):
        if self.title:
            return self.title
        return 'タイトル名なし・blog id : ' + str(self.id)


# Like Blog
class LikeBlog(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True)
    blog = ForeignKey(Blog, on_delete=CASCADE, null=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    constraints = [
        UniqueConstraint(fields=['user', 'blog'], name='unique_like_blog'),
    ]

    def __str__(self):
        return self.user.username + '・blog id : ' + str(self.blog.id)


# Blog Comment
class BlogComment(Model):
    blog = ForeignKey(Blog, on_delete=CASCADE, null=False)
    # user = ForeignKey(User, on_delete=SET_NULL, null=True)
    content = TextField(blank=True, null=True)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return 'blog id : ' + str(self.blog.id)
