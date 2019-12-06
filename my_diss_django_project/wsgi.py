"""
WSGI config for my_diss_django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

#Add project directory to python path
path = '/home/cupcakecode/my_diss_django_project/'
if path not in sys.path:
  sys.path.append(path)

#move to the project diretory
os.chdir(path)

#tell django where the setting.py module is


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_diss_django_project.settings')

#set up Django
import django
django.setup()

#import django to handle requests
import django.core.handlers.wsgi
application=django.core.handlers.wsgi.WSGIHandler()