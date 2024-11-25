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


# The request parameter is named like this so we can later use request.method to specify the type of request (POST
# or GET)
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
    # "Comments" in post.comments.all() is the related name for comments in the Post model. Called a "reverse lookup"
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()


    if request.method == "POST":
        # instance of the CommentForm class using the form data that was sent in the POST request
        comment_form = CommentForm(data=request.POST)
        # valid: The form has been filled out correctly
        if comment_form.is_valid():
            # Commit=False as we still need to edit the comment with the author and post as below
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )


    # Resets the content of the form to blank so that a user can write a second comment if they wish
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