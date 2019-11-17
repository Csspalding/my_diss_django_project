from django.contrib import admin
from cupcake_site.models import Category
from cupcake_site.models import Page
from cupcake_site.models import UserProfile



class PageAdmin(admin.ModelAdmin):
  list_display = ('title','description','category', 'url')

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug':('name',), }
  
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'id') 
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

