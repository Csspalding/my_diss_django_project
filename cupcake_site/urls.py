from django.urls import path
from cupcake_site import views
#created 01/08/19 by Cass
#this file handles urls that startwith rango/  

app_name = 'cupcake_site'
#note the about/ NOT about  - this syntax is very important was the issue with the test not working
urlpatterns = [
    path('', views.index, name='index'), #this url points to the index view function
    path('about/', views.about, name='about'),
]
