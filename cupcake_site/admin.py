from django.contrib import admin
from cupcake_site.models import Category, Page
#from rango.models import UserProfile
# Register your models here.


class PageAdmin(admin.ModelAdmin):
  list_display = ('title','description','category', 'url')

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# admin.site.register(UserProfile)

