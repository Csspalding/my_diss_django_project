from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User #PostAuthor, CommentAuthor
from cupcake_site.models import UserProfile
from django.template.defaultfilters import slugify

"""Azzopardi & Maxwell "Tango with Django" (2019) & Traversy Media (2017) tutorial helped with these post models"""
#Meta inner class helps get rid of the extra default 's' on Postss, as displayed on /admin page 
"""Status and Display choices adapted from The Abhijeet https://github.com/TheAbhijeet/Django_blog/blob/master/blog/models.py"""
#post has one author but authors have many posts, relationship is ForeignKey to userprofile
#For the slug Adding unique=True attrubute after database is created avoids database conflicts, as posts are only for registered users. 

STATUS = (
        (0, "Draft"),
        (1, "Publish")
)

      
class Posts(models.Model):
    title = models.CharField(max_length=200, blank=True)# choices=DISPLAY, default=1)
    slug = models.SlugField(max_length=200, blank=True)#add unique=true attribute after database is created.
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)# so posts can be in published or draft status
    post_image = models.ImageField(upload_to ='post_images/', blank=True)

    class Meta:
        verbose_name_plural = "Posts"
        ordering=['-created_at']
        

    def __str__(self):
        return self.title

    #To display the post title with a clean slug instead of default post id 
    def save(self, *args, **kwargs,):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    #To display a default picture when a user does not load one
    def picture_or_default(self, default_path="/static/images/digitalcakes.jpg"):
        if self.picture:
            return self.picture
        return default_path
      



        