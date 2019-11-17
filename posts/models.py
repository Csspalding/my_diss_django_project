from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User # PostAuthor and CommentAuthor
from cupcake_site.models import UserProfile
from django.template.defaultfilters import slugify
#from django.utils.decorators import method_decorator

#Tango book & travery media tutorial helped with these post models
#Meta inner class helps get rid of the extra default 's' on Postss, as displayed on /admin page 
# Status and Display choices adapted from The Abhijeet https://github.com/TheAbhijeet/Django_blog/blob/master/blog/models.py
#post has one author but authors have many posts, relationship is ForeignKey to userprofile
#For the slug Adding unique=True attrubute after database is created avoids database conflicts, as posts are only for registered users, this are constrained to a userprofile instance existing

STATUS = (
        (0, "Draft"),
        (1, "Publish")
)
DISPLAY = (
        (0, "No"),
        (1, "Yes")
)

#"""Model for Blog Posts"""       
class Posts(models.Model):
    title = models.CharField(max_length=200, blank=True)# choices=DISPLAY, default=1)
    slug = models.SlugField(max_length=200, blank=True)#add unique true attribute after database is created.
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)#TODO add helper text to explain display /draft
    post_image = models.ImageField(upload_to ='post_images/', blank=True)

    class Meta:
        verbose_name_plural = "Posts"
        ordering=['-created_at']
        # / or ordering by likes?
        #ordering = ['-id'] # or ordering by ['last_modified']

    def __str__(self):
        return self.title

    #To display the post title with a clean slug instead of default post id 
    def save(self, *args, **kwargs,):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)
    
    #TODO not working or rendering
    def picture_or_default(self, default_path="/static/images/digitalcakes.jpg"):
        if self.picture:
            return self.picture
        return default_path
        #{{ user.picture_or_default }} in template

#https://stackoverflow.com/questions/14170473/get-absolute-url-in-django-when-using-class-based-views"""
    #@models.permalink

    #Django Projects Cookbook   
    #def __unicode__(self):
       # return self.name or str(self.id)

    #Django Docs    
    #def get_absolute_url(self):
        #return reverse('posts.views.PostDetail',args=[str(self.id)])

        #return reverse('people.views.details', args=[str(self.id)])
 #-user-when-creating-an-object-in-django-admin
#with this code I may not need to set an created_by_attribute in populatePostsDb.py
    # def save_model(self, request, obj, form, change):
    #     if not obj.created_by_user:
    #         obj.created_by_user = request.user
    #     obj.save() 

#Comment code adapted from https://realpython.com/get-started-with-django-1/

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')#the author of the comment, one author one comment, NB user.username is the 
#     #author = models.CharField(max_length=60)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Posts', on_delete=models.CASCADE)#post.id is id, do not post.user for user instead its user_author.username see comment below
    
#     class Meta:
#         verbose_name_plural = "Comments"
        
#         ordering=['-created_at']

#     def __str__(self):
#         return self.author # .auth.models import User as registered by redux package


        