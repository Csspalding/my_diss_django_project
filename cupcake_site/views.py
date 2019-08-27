from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic import CreateView

from cupcake_site.models import Category, Page
from cupcake_site.forms import CategoryForm, PageForm
#view handles responce to request from client


#index view is the home page for the project
def index(request):
  #construct a dictionary to pass to the template engin as its context.
  context_dict= {'boldmessage':'did you know... you can learn coding skills for free...'}
  return render(request, 'cupcake_site/index.html', context=context_dict)


class AboutView(View):
  def get(self, request):
    context_dict={'boldmessage': 'We need more women in tech'}
    return render(request, 'cupcake_site/about.html', context=context_dict)


def h(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/h.html', context=context_dict)


#Learning Tools 
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
  context_dict={'boldmessage': 'There are many Free Learning Tools On-Line, click on a category below to see the links.'}
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


def add_page(request, category_name_slug):
  try:
    category = Category.objects.get(slug=category_name_slug)
  except Category.DoesNotExist:
    category = None

  form = PageForm()
  if request.method =='POST':
    form = PageForm(request.POST)

    if form.is_valid():
      if category:
        page = form.save(commit=False)
        page.category = category
        page.view =0
        page.save()
    #once page form is created redirect user to the show_category() view, if a match is found from show_category ()the complete url is returned
    #as an added complication show_category(category_name_slug) passed in parameter, by providing a value in dictionary as kwargs to the reverse function it can formulate the url
        form.helper.form_action = reverse('url_name', kwargs={'category_name_slug': category_name_slug})
        return redirect(reverse('cupcake_site:show_category', kwargs={'category_name_slug':category_name_slug}))
        #return show_category(request, category_name_slug)
    else:
      print (form.errors)

  context_dict = {'form':form, 'category':category} #objects passed through the template context dictionary to the html
  return render(request, 'cupcake_site/add_page.html',context=context_dict)

#Error get() missing 1 required positional argument: 'category_name_slug'
# class PageCreateView(CreateView): 
#     #@method_decorator(login_required)
#     def get_page_cat(self, category_name_slug):#helper method to get the category slug
#       try:
#         category_slug = Category.objects.get(slug=category_name_slug)
#       except Category.DoesNotExist:
#         category = None
#       return category_name_slug

#     #@method_decorator(login_required)
#     def get(self, request, category_name_slug):
#       try:
#         slug = self.get_page_cat(self, category_name_slug)#get the category learning tool the page adds on to
#       except TypeError:
#         return redirect('cupcake_site/tools.html')#if there is an error redirect them to learning tools page

#       form=PageForm()
#       context_dict = {'form': form, 
#                   'slug':slug}
#       return render(request, 'cupcake_site/add_page.html', context_dict)
      
    # #@method_decorator(login_required)
    # def post(self, request, category_name_slug):
    #   try:
    #     (form, slug)=self.get_page_cat(category_name_slug)
    #   except TypeError:
    #     return redirect('cupcake_site/tools.html')
    #   form= PageForm(request.POST)

    #   if form.is_valid():
    #     form.save(commit=True)
    #     #return render(request, 'cupcake_site/tools.html') 
    #     return redirect(reverse('tools/<slug:category_name_slug>',kwargs={'category_name_slug': category_name_slug}))
    #   else:
    #     print(form.errors)
    #   context_dict = {'form': form, 
    #               'slug':slug}
    #   return render(request, 'cupcake_site/add_page.html', context_dict) 

     
#Class to create and process the Form to add a new Category to Learning Tools       
class CategoryCreateView(CreateView):
    #@method_decorator(login_required)
    def get(self, request):
      form=CategoryForm()
      return render(request, 'cupcake_site/add_category.html', {'form': form})

    #@method_decorator(login_required)
    def post(self, request):
      form= CategoryForm(request.POST)

      if form.is_valid():
        form.save(commit=True)
        return tools(request)
      else:
        print(form.errors)
      return render(request, 'cupcake_site/add_category.html', {'form': form})  
   
#TODO
# def register_profile():
#     return 
# def profile(request):
#   context_dict={}
#   return render(request, 'cupcake_site/profile.html', context= context_dict)