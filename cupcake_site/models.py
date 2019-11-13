from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


from django.utils import timezone

class Category(models.Model):
  # Category fields these are attributes/ data columns in the database
  name = models.CharField(max_length=128, unique=True)
  views = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)
  slug = models.SlugField(unique=True)# warning cannot add this unique TRUE attribute til after the database is created and populated as this unique constraint would been violated
 
  def save(self, *args, **kwargs):
    #override save() so if the category changes so does it's slug for clean url's 
    self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)

  #changes the spelling of Categorys to Learning Tools
  class Meta:
    verbose_name_plural = 'Learning Tools'
    
#string method prints out the category name
  def __str__(self):
    return self.name


class Page(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    #changes spelling for Pages to Page
    class Meta:
      verbose_name_plural = 'Pages'
   
    #string method prints out the page title
    def __str__(self):
        return self.title


# UserProfile links to django.contrib.auth.models.User instance of User model
class UserProfile(models.Model):
    # a user attribute is required
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #other 3 attributes are user biography, email and picture 
    bio = models.CharField(max_length=5000, blank=True)
    email = models.EmailField(blank=True)
    #upload_to store user images in the project MEDIA_ROOT
    picture = models.ImageField(upload_to='profile_images/' , blank=True)
    
    #set a default profile pic image https://stackoverflow.com/questions/13090505/render-default-image-django
    def picture_or_default(self, default_path="/static/images/no_user_image.jpg"):
        if self.picture:
            return self.picture
        return default_path
        #{{ user.picture_or_default }} in template

    class Meta:
        verbose_name_plural = 'User Profiles'
       
    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

    #order_with_respect_to = 'post.id' //for a function if I want to show blog posts later?
 