from django import forms
from string import Template
from django.utils.safestring import mark_safe
from my_diss_django_project import settings
from cupcake_site.models import User
from posts.models import Comment
from crispy_forms.helper import FormHelper
from django.core.files.images import get_image_dimensions

#adapted to a crispy CreateViewfrom https://realpython.com/get-started-with-django-1/
class CommentForm(forms.ModelForm):
    # author = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Your Name"
    #     })
    # )
    
    model=Comment
    #fields = ('body',)
    

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Was this article useful? Any comments?"
        })
    )