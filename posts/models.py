from django.db import models
from datetime import datetime

# Create your models here.
    

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    #last_modified = models.DateTimeField(auto_now=True)
    #categories = models.ManyToManyField('Category', related_name='posts')

#To display the blog post title of each of the items listed in Posts instead of default Post Object 1,2,3 in our model
    def __str__(self):
        return self.title

#to save the model unit eg 'Blog' as a plural, (default adds an s) add this code and get rid of the extra 's' on /admin page 
    class Meta:
        verbose_name_plural = "Posts"

#todo test change app name displayed to Blog instead of Posts

# class Category(models.Model):
#     name = models.CharField(max_length=20)


# class Comment(models.Model):
#     author = models.CharField(max_length=60)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)