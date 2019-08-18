from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#index view is the home page for the project
#view handles responce to request from client


def index(request):
  #construct a dictionary to pass to the template engin as its context.
  #Note the key boldmessage is the {{boldmessage}} in the index.html template
  context_dict= {'boldmessage':'did you know... you can learn coding skills for free...'}
 
  return render(request, 'cupcake_site/index.html', context=context_dict)
 
def about(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/about.html', context=context_dict)

def h(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/h.html', context=context_dict)
#now map your Url to the view rango/about.html