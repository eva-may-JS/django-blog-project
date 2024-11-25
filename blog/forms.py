from .models import Comment
from django import forms

# Our CommentForm class will inherit from the Django forms.ModelForm class
class CommentForm(forms.ModelForm):
    # We can just use the meta field to tell the ModelForms class what models and fields we want in our form
    class Meta:
        # Our Comments model in models.py
        model = Comment
        # The body field from our Coments model
        fields = ('body',)