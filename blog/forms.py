from django import forms
from .models import Comment


# Our CommentForm class will inherit from the Django forms.ModelForm class
class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """

    # We can just use the meta field to tell the ModelForms class what models and fields we want in our form
    class Meta:
        """
        Specify the django model and order of the fields
        """
        
        # Our Comments model in models.py
        model = Comment
        # The body field from our Coments model
        fields = ('body',)