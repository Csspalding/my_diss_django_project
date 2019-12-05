from django.contrib import admin
from posts.models import Posts
from cupcake_site.models import UserProfile

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','created_at', 'last_modified','user' )
    list_filter=("status",)
    prepopulated_fields = {'slug':('title',)} 

admin.site.register(Posts, PostsAdmin)




