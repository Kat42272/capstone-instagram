from django import forms
from . import models

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = models.InstaProfileModel
        fields = ['bio', 'email', 'phone', 'picture']
