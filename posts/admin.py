from django.contrib import admin
from posts.models import Posts
#from posts.models import Comment


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','created_by','created_at', 'last_modified' )
    list_filter=("status",)
    #-user-when-creating-an-object-in-django-admin
#with this code I may not need to set an created_by_attribute in populatePostsDb.py
    # def save_model(self, request, obj, form, change):
    #     if not obj.created_by_user:
    #         obj.created_by_user = request.user
    #     obj.save()   
    
#add comments section to site admin so comments can be moderated if necessary
# class CommentAdmin(admin.ModelAdmin):
    # list_display = ('post', 'body')
    # pass

admin.site.register(Posts, PostsAdmin)


#admin.site.register(Comment, CommentAdmin)

