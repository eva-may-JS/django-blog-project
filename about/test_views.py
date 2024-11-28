from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    # setUp: method we can use in our tests to provide initial settings for our tests to use
    def setUp(self):
        """Creates about me content"""
        self.about_content = About(title="About Me", 
                         content="This is about me")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"This is about me", response.content)
        # response.context: checks that the correct objects were passed to the template by the view
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)


    def test_successful_collaboration_request_submission(self):
        """Test for user sending a collaboration request in the About page"""

        post_data = {
            'name': 'Tess',
            'email': 'test@test.com',
            'message': 'This is my message'
        }
        # POST request tests need an additional argument, which is the data being POSTed
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content
        )