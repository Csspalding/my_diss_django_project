from django import forms
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField
from my_diss_django_project import settings
from cupcake_site.models import User
from posts.models import Posts
#from posts.models import Comment
from crispy_forms.helper import FormHelper
from django.core.files.images import get_image_dimensions

class PostForm(forms.ModelForm):
    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #when a post is made it wont yet have instance of a user unless already registered
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.helper = FormHelper()
    
    class Meta:
        model = Posts
        fields = ('title', 'body')
    # TODO status image


#adapted to a crispy CreateViewfrom https://realpython.com/get-started-with-django-1/
#class CommentForm(forms.ModelForm):
    # author = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Your Name"
    #     })
    # )
    
    #model=Comment
    #fields = ('body',)
    

    # body = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         "class": "form-control",
    #         "placeholder": "Any comments?"
    #     })
    # )