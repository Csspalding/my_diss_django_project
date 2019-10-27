from django.urls import path
from django.urls import re_path
from posts import views

#Latest Posts Index Page  

#Anything that starts with details, the data for each post in the db,  will check ?,  P parameter  Django gives an automatic id which autoincrements in the datebase as each new post is added to the blog 
app_name = 'posts'

urlpatterns = [
  path('', views.posts_index, name='posts_index'), 
  re_path(r'^posts_details/(?P<id>[0-9])/$', views.posts_details, name= 'posts_details'), 
  path('add_post/', views.PostCreateView.as_view(),name = 'add_post'), 
]
  
  
  #THIS IS THE WRONG PATH - this is create the view of a post, and a form to amend it
  #path('add_post', views.PostCreateView.as_view(), name='add_post'),
  #TODO allow posts to be searched on title slug OR keep search on id?
  #add comments to posts
  #add likes/views to posts
  #Add a search to the site
  #TESTING