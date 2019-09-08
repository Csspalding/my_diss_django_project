from django.contrib import admin
from posts.models import Posts
#from posts.models import Comment


# class PostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'id','status', 'created_at' )
    # list_filter=("status",)
     #not using yet  #search_fields=['title', 'body']
                     #prepopulated_fields={'slug':('title',)}
    
    
#add comments section to site admin so comments can be moderated if necessary
# class CommentAdmin(admin.ModelAdmin):
    # list_display = ('post', 'body')
    # pass

admin.site.register(Posts)
#admin.site.register(PostAdmin)
#admin.site.register(Comment, CommentAdmin)

