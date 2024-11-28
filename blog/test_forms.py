# Django's testing library
from django.test import TestCase
# This imports the comment form we created so we can test it.
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Tests whether our comment form responds correctly to valid and invalid comment entry attempts
    """
    # test class method names must begin with "test_"
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'Hello'})
        # this message will be printed out on failure
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': 't'})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')