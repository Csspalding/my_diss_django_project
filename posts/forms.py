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
        fields = ('title', 'body', 'post_image')

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        # kwargs.pop  has key error userprofile  - changed to kwargs.get error is init gets unexpected argument request
        self.author_post = kwargs.pop('user')
        #author_post = self.form(author_post=author_post)
        super(PostCreateForm, self).__init__(*args, **kwargs)

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     #if Posts.objects.filter(author_post=self.author_post, title=title).exists():
    #     #error cannot resolve keywork into field user/ userprofile /username BUT when I use author_post= Error is cannot query Cassie2  must use UserProfile instance
    #     #profile = request.user.get_profile()
    #     if Posts.objects.filter(title=title).exists():
    #         raise forms.ValidationError("You have already written a post with same title.")
    #     return title

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

   