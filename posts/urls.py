from django.urls import path
from django.urls import re_path
from django.conf.urls import *
#from django.contrib.auth.views import login, logout, password_change, password_reset
from posts.views import PostCreate, PostDetail
from posts import views


#Latest Posts Index Page  

#Anything that starts with details, the data for each post in the db,  will check ?,  the P parameter which is a Django automatic id which autoincrements in the datebase as each new post is added 

#pattern name should be of the form appname_viewname
app_name = 'posts'

urlpatterns = [
  # path('', views.hello_world, name='hello_world'),
  path('', views.posts_index, name='posts_index'),  
  path('posts_create/', views.PostCreate.as_view(),name = 'posts_create'), 
  path('posts_detail/<int:id>', views.PostDetail.as_view(), name='posts_detail'), 
   #path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
]

  #add comments to posts
  #add likes/views to posts
  #Add a search to the site
  #TESTING