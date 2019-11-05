from django.urls import path
from django.urls import re_path
#from django.generic.views import CreateView
from posts import views
from django.utils.translation import gettext_lazy as _


#Latest Posts Index Page  

#Anything that starts with details, the data for each post in the db,  will check ?,  the P parameter which is a Django automatic id which autoincrements in the datebase as each new post is added 

app_name = 'posts'

urlpatterns = [
  path('', views.posts_index, name='posts_index'), 
  re_path(r'^posts_details/(?P<id>[0-20])/$',views.posts_details, name='posts_details'), 
  path('add_post/', views.PostCreateView.as_view(),name = 'add_post'), 
]

  #add comments to posts
  #add likes/views to posts
  #Add a search to the site
  #TESTING