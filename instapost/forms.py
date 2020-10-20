from django import forms
from . import models
from comments import models
class AddPostForm(forms.ModelForm):    
    class Meta:        
        model = models.PostModel       
        fields = ['caption', 'picture']


class AddNewCommentForm(forms.Form):  
        body = forms.CharField(max_length=280, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'comment ....'
        }
    ))
