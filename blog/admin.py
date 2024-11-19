from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.

# This will allow to create, update and delete blog posts from the admin panel. Commented out as we have now 
# registered it above with the decorator @admin.register(Post)
# admin.site.register(Post)
admin.site.register(Comment)