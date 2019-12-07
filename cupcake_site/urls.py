from django.urls import path
from cupcake_site import views
#from cupcake_site.views import AboutView #always import seperately 
#from cupcake_site.views import IndexView  

"""@author Cassie Spalding 2140148s dissertation project 2019 
this file handles urls that startwith cupcakesite/ """

"""note regarding django registration redux, url patterns - see login.html and other templates in templates/registration dir"""

app_name = 'cupcake_site'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('about/', views.AboutView.as_view(), name='about'),
    path('career/', views.career, name='career'),
    path('tools/', views.tools, name='tools'),
    path('tools/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/',views.CategoryCreateView.as_view(), name='add_category'),
    path('tools/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register_profile/', views.RegisterProfileCreateView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileCreateView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('cupcake_tutorial/', views.TutorialView.as_view(), name='cupcake_tutorial'),
    path('search/', views.SearchView.as_view(), name='search'),
    
]  

