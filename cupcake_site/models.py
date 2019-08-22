from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here, which make tables and relationships in the database
class Category(models.Model):
  #fields in a Category these are attributes, data columns in the database
  name = models.CharField(max_length=128, unique=True)
  views = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)
  slug = models.SlugField()# warning cannot add this unique TRUE attribute til after the database is created and populated as this unique constraint would have been violated
 

  def save(self, *args, **kwargs):
    #override save() so if the category changes so does it's slug for clean url's 
    self.slug = slugify(self.name)
    super(Category, self).save(*args, **kwargs)

  #changes the spelling of Categorys to Categories
  class Meta:
    verbose_name_plural = 'Learning Tools'#Categories
    
#string method prints out the category name
  def __str__(self):
    return self.name


class Page(models.Model): 
  #fields in a Page
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

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images' , blank=True)

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.user.username

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

