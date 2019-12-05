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

     
# https://stackoverflow.com/questions/13460426/get-user-profile-in-django    
# a=User.objects.get(email='x@x.xom')
# a.get_profile().DOB will give the dateofbirth value from extrauser table.



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

   