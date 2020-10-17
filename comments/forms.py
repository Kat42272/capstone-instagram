from django import forms
from . import models

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ['body']