from django.contrib import admin
from .models import Post

# Register your models here.

# This will allow to create, update and delete blog posts from the admin panel
admin.site.register(Post)
