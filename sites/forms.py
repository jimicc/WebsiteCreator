from django import forms
from . import models

class CreateWebsite(forms.ModelForm):
    class Meta:
        model = models.Website
        fields = ['title', 'image']
