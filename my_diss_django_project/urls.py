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


class MyRegistrationView(RegistrationView):
    #@method_decorator(login_required)
    def get_success_url(self, user):
      return reverse( 'cupcake_site:register_profile')

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cupcake_site/', include('cupcake_site.urls')),#urls startwith 'cupcake_site/' are handled by cupcake_site app
    path('posts/', include('posts.urls')),#urls startwith 'posts/' are handled by posts app
    path('admin/', admin.site.urls),

    #override the existing registration_register URL mapping from redux package
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),

    path('accounts/',include('registration.backends.simple.urls'))#out of the box django-registration-redux package for user authentication and login etc
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


