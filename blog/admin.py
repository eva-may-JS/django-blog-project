from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# This will allow to create, update and delete blog posts from the admin panel
admin.site.register(Post)
admin.site.register(Comment)