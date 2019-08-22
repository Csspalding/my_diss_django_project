from django.shortcuts import render
from django.http import HttpResponse
from cupcake_site.models import Category, Page
# Create your views here.
#index view is the home page for the project
#view handles responce to request from client


def index(request):
  #construct a dictionary to pass to the template engin as its context.
  context_dict= {'boldmessage':'did you know... you can learn coding skills for free...'}
 
  return render(request, 'cupcake_site/index.html', context=context_dict)
 
def about(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/about.html', context=context_dict)

def h(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/h.html', context=context_dict)

def tools(request):
  #get all the categories, later maximum 10 [:10]
  category_list = Category.objects.all()#can order by likes
  page_list = Page.objects.order_by('views')[:5]
  #category_list = Category.objects.order_by('-likes')[:5]
  #save them
  context_dict ={}
  context_dict ['categories'] = category_list
  context_dict ['pages'] = page_list
  
  return render(request, 'cupcake_site/tools.html', context=context_dict)

def show_category(request, category_name_slug):
  context_dict={'boldmessage': 'Many Free Tools On-Line'}
  try:
    # get () returns DoesNotExist or instance // try/catch  handles exception if no categories exist
    category= Category.objects.get(slug=category_name_slug)
    #filter()  will return a list of page objects or an empty list
    pages= Page.objects.filter(category=category)
    #Save results from filter() 
    context_dict['pages'] = pages
    #add the category object from db to the context dictionary
    # which is used to verify it exists in the template 
    context_dict['category']= category
  except Category.DoesNotExist:
    #set context_dict to None as none found, DoesNotExist exception is displayed
    context_dict['pages'] = None 
    context_dict['category']= None 
  return render(request, 'cupcake_site/tools_category.html', context=context_dict)
#now map your Url to the view rango/about.html


   