from django.urls import path
from cupcake_site import views
#from cupcake_site.views import AboutView #always import seperately 
#from cupcake_site.views import IndexView  

"""created 01/08/19 by Cassie Spalding, this file handles urls that startwith cupcakesite/ """

"""note regarding django registration redux, url patterns - see login.html and other templates in templates/registration dir"""

app_name = 'cupcake_site'

urlpatterns = [
    #path('', views.index, name='index'), #this url points to the index view function
    path('', views.IndexView.as_view(), name='index'), 
    path('about/', views.AboutView.as_view(), name='about'),
    path('h/', views.h, name='h'),#carsole  todo place this in a template tag on About later
    path('tools/', views.tools, name='tools'),
    path('tools/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/',views.CategoryCreateView.as_view(), name='add_category'),
    path('tools/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register_profile/', views.RegisterProfileCreateView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileCreateView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
]  

