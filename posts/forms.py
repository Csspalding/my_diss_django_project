from django import forms
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField
from my_diss_django_project import settings
from cupcake_site.models import User
from posts.models import Posts
from crispy_forms.helper import FormHelper
from django.core.files.images import get_image_dimensions

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('slug', 'user')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
       
    def clean_title(self):
        title = self.cleaned_data['title']
        if Posts.objects.filter(user=self.user, title=title).exists():
            raise forms.ValidationError("You have already written a post with the same title.")
        return title

     
