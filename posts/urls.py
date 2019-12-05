from django.urls import path
from posts.views import PostCreate, PostDetail
from posts import views



app_name = 'posts'

urlpatterns = [
 
  path('', views.posts_index, name='posts_index'),  
  path('posts_create/', views.PostCreate.as_view(),name = 'posts_create'), 
  path('posts_detail/<int:pk>', views.PostDetail.as_view(), name='posts_detail'), 
]
