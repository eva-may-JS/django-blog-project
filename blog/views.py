from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1)
    template_name = "blog/index.html"
    paginate_by = 6


# The slug parameter gets the argument value from the URL pattern named post_detail
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()


    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )


    comment_form = CommentForm()

    # render combines the chosen template with the dictionary object specified, in this case {"post": post},
    # so the information in the dictionary can be inserted into the template
    return render(
        request,
        # path to the template file
        "blog/post_detail.html",
        # This {'post': post} object is called "context", and is then available for use in the template as 
        # the DTL variable {{ post }}
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )