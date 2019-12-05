from django import forms
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField
from my_diss_django_project import settings
from cupcake_site.models import Page
from cupcake_site.models import Category
from cupcake_site.models import User
from cupcake_site.models import UserProfile
from crispy_forms.helper import FormHelper
from django.core.files.images import get_image_dimensions

"""Learning Tools category form to add another category"""
class CategoryForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Please enter the category name.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  slug = forms.CharField(widget=forms.HiddenInput(), required=False)
  
  
  """Specify model for form, and visible fields to be displayed""" 
  class Meta:
    model = Category
    fields = ('name',)

"""Learning Tools form to add a new Page link"""
class PageForm(forms.ModelForm):
  title = forms.CharField(max_length=128, help_text="Please enter the title of the web page.")
  description = forms.CharField(max_length=500, help_text="Describes why this page is a great resource to help direct others towards useful information.")
  url = forms.URLField(max_length=200, help_text="Please enter the web address of the page you want to add, starts with http:// Hint: you can copy and paste the link from your browser.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

  class Meta:
    model = Page
    exclude = ('category',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  """override the form to handle missing data/ default fields for the url""" 
  def clean(self):
    cleaned_data = self.cleaned_data
    url = cleaned_data.get('url') 
    #Note: the get function will return None if user enters nothing as new form will not exist

    """HANDLING SECURE https:// too!
    if the url is not empty and doesn't start with 'http://' then automatically input 'http://'  """
    if url and not (url.startswith('http://') or url.startswith('https://')):
      url = 'http://'+ url
      cleaned_data['url'] = url
      #always end clean() by returning a reference to the cleaned_data dictionary
      return cleaned_data

""" """
class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())#hides password as it is typed
 
  """For passing variable number of arguments and keyword dictionary arguments in the function """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  class Meta:
    model = User
    fields = ('username','password', 'email') 
    #A userprofile is only created once the user is registered

#create a widget to render the photo
#https://stackoverflow.com/questions/28764571/display-image-from-imagefield-by-means-of-form

class ImageUploadForm(forms.Form):
  profile_photo = forms.ImageField()


# class PictureWidget(forms.widgets.Widget):
#     def render(self, name, value, attrs=None, renderer=None):
#         html = Template("""<img src="$media$link"/>""")
#         return mark_safe(html.substitute(media=settings.MEDIA_URL, link=value))

class UserProfileForm(forms.ModelForm):#when a userprofile is made it wont yet have instance of a user unless already registered
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()   

  class Meta:
    model = UserProfile
    fields = ('bio', 'picture')
    #TODO test clean_pic function
    #clean_pic=('picture')
   

    #https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django/6396744
    def clean_pic(self):
        pic = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(pic)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = pic.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')
            #validate file size
            if len(pic) > (20 * 1024):
              raise forms.ValidationError
            (u'Your Profile picture file size may not exceed 20k.')

        except AttributeError:
            pass
            """
            Handles case when updating the user profile
            and does not supply a new profile picture
            """

        return pic
