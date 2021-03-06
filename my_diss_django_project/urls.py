"""my_diss_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from registration.backends.simple.views import RegistrationView
from django.urls import reverse
from cupcake_site import views 
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


"""override redux package existing registration_register (when users Sign Up) to redirect to a custom user profile registration form"""
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
      return reverse( 'cupcake_site:register_profile')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cupcake_site/', include('cupcake_site.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),#override existing redux package URL mapping
    path('accounts/', include('registration.backends.simple.urls')),#out of the box django-registration-redux package for user authentication and login etc
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# path for Media files 


