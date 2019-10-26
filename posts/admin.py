from django.contrib import admin
from posts.models import Posts
#from posts.models import Comment


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','author_post','created_at', 'last_modified' )
    list_filter=("status",)
    prepopulated_fields = {'slug':('title',)} 
    #inlines = [PostCommentsInline]


     
    
#add comments section to site admin so comments can be moderated if necessary
# class CommentAdmin(admin.ModelAdmin):
    # list_display = ('post', 'body')
    # pass
#class TagsAdmin(admin.ModelAdmin):
    #list_display = ('name', 'slug')

admin.site.register(Posts, PostsAdmin)


#admin.site.register(Tags, TagsAdmin)
#admin.site.register(Comment, CommentAdmin)

