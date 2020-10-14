from django import forms
from . import models

class EditPostForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ['caption', 'picture']
