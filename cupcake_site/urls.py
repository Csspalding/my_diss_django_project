from django.urls import path
from cupcake_site import views
from cupcake_site.views import AboutView #always import seperately 

#created 01/08/19 by Cass
#this file handles urls that startwith cupcakesite/  

app_name = 'cupcake_site'
#note the about/ NOT about  - this syntax is very important was the issue with the test not working
#url as_view() is part of the base View class provides Django engine necessary code to access views.py classes get() function
urlpatterns = [
    path('', views.index, name='index'), #this url points to the index view function
    path('about/', views.AboutView.as_view(), name='about'),
    path('h/', views.h, name='h'),
    path('tools/', views.tools, name='tools'),
    path('tools/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/',views.CategoryCreateView.as_view(), name='add_category'),
    path('add_page/',views.PageCreateView.as_view(), name='add_page'),
    #path('profile/',views.profile, name='profile')#user can see/edit their profile
]


#from rango import views
#created 01/08/19 by Cass
#this file handles urls that startwith rango/  

# app_name = 'rango'
# #note the about/ NOT about  - this syntax is very important was the issue with the test not working
# urlpatterns = [
#     path('', views.index, name='index'), #this url points to the index view function
#     path('about/', views.about, name='about'),
#     path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
#     path('add_category/', views.add_category, name='add_category'),
#     path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('restricted/', views.restricted, name='restricted'),
#     path('logout/', views.user_logout, name='logout'),
# ]
