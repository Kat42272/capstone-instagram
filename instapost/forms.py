from django import forms
from . import models

class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ['caption', 'picture']
