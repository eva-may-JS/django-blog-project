from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    # use to build a URL for each post
    slug = models.SlugField(max_length=200, unique=True)
    # cascade on delete means if user is deleted, so are all their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    # This field holds the URL to the pictures we are storing on Cloudinary
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    # The auto_now_add=True means the default created time is the time of post entry.
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single blog post comment entry related to :model:`auth.User` and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"