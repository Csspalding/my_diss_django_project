from django.contrib import admin
from posts.models import Posts
from cupcake_site.models import UserProfile
#from posts.models import Comment

# class PostCommentsInline(admin.TabularInline):
#     model = PostAuthor
#     max_num = 0

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','created_at', 'last_modified','author_post' )
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

