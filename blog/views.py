from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


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

    # render combines the chosen template with the dictionary object specified, in this case {"post": post},
    # so the information in the dictionary can be inserted into the template
    return render(
        request,
        # path to the template file
        "blog/post_detail.html",
        # This {'post': post} object is called "context", and is then available for use in the template as 
        # the DTL variable {{ post }}
        {"post": post},
    )