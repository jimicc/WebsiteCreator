from django import forms
from . import models

class CreateWebsite(forms.ModelForm):
    class Meta:
        model = models.Website
        fields = [
            'title',
            'slug',
            'link_1',
            'link_2',
            'background_image',
            'image_service_1',
            'title_service_1',
            'text_service_1',
            'image_service_2',
            'title_service_2',
            'text_service_2',
            'parallax_image',
            'link_2_title',
            'link_2_content',
            'link_2_tab_opt_1',
            'link_2_tab_opt_2',
            'link_2_tab_content_1',
            'link_2_tab_content_2',
            'email',
            'phone',
            ]
        widgets = {'slug': forms.HiddenInput()}
