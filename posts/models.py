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
    slug = models.SlugField(max_length=200)#add unique true later
    body = models.TextField()
    # a user attribute is required
    created_by = models.OneToOneField(User,on_delete=models.CASCADE) 
    #Not correct //created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
   
    
#To display the blog post title of each of the items listed in Posts instead of default Post Object 1,2,3 in model
#to handle the case of no author adapted from  #o_c https://stackoverflow.com/questions/937954/how-do-you-specify-a-default-for-a-django-foreignkey-model-or-adminmodel-field
    def save(self, *args, **kwargs):
    #   #override save() so if the title changes so does it's slug  
      self.slug = slugify(self.title)
#       if self.author is None:  # Set default reference if author is None
      super(Posts, self).save(*args, **kwargs)
    #     self.author = User.objects.get(id=1) 
   

    def __str__(self):
        return self.title

#Tango book & travery media tutorial
#add this code and get rid of the extra default 's' on Postss, as displayed on /admin page 
    class Meta:
        verbose_name_plural = "Posts"
        #ordering=['-created_at']/ or ordering by likes?


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
        