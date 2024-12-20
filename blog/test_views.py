from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):

    # setUp: method we can use in our tests to provide initial settings for our tests to use
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        # Reverse generates a URL for accessing post_detail view, providing 'blog-title' (slug) as an argument.
        # Then, self.client.get() sends a GET request to the post_detail view
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        # response.context: checks that the correct objects were passed to the template by the view
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    
    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        # User must be logged in to comment, so test simulates logging the user in to carry out the test
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        # POST request tests need an additional argument, which is the data being POSTed
        response = self.client.post(reverse(
            'post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )