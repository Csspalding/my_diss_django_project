from django.urls import path, re_path
from posts import views


#from . import views
# . import the dot means import all methods in posts.views.py

app_name = 'posts'

urlpatterns = [
  # local host extension: /posts/ , passes to the posts_index method in  Posts views.py file     
  path('', views.posts_index, name='posts_index'), 

  re_path(r'^posts_details/(?P<id>[0-9])/$', views.posts_details, name= 'posts_details'),
  #Anything that starts with details, the data for each post in the db,  will check P parameter  Django gives an automatic id which autoincrements in the datebase as each new post is added to the blog 
]
