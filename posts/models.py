from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



#adapted from The Abhijeet https://github.com/TheAbhijeet/Django_blog/blob/master/blog/models.py#

STATUS = (
        (0, "Draft"),
        (1, "Publish")
)
    
class Posts(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)#add unique true attribute after database is created to avoid database errors as Posts has User as ForeignKey, so a User has to be created prior to a post being created.
    body = models.TextField()
    # a user attribute is required
    author_post = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1) #default to publish for now
    #featured_image = models.ImageField(upload_to='static/blog/uploads/%Y/%m/%d/', blank=True, null=True)
   
#To display the post title with a clean slug instead of default Post Object 1,2,3 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)
    
#Tango book & travery media tutorial
#add this code and get rid of the extra default 's' on Postss, as displayed on /admin page 
    class Meta:
        verbose_name_plural = "Posts"
        #ordering=['-created_at']/ or ordering by likes?
       # ordering = ['-updated_on'] # or ordering by ['last_modified']

    def __str__(self):
        return self.title
    


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
        