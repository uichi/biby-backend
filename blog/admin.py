from django.contrib import admin
from .models import Blog, LikeBlog, BlogComment

admin.site.register(Blog)
admin.site.register(LikeBlog)
admin.site.register(BlogComment)
