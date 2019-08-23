from django.shortcuts import render
from django.http import HttpResponse
#from django.utils.decorators import method_decorator
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic import CreateView

from cupcake_site.models import Category, Page
from cupcake_site.forms import CategoryForm, PageForm
# Create your views here.

#index view is the home page for the project
#view handles responce to request from client


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


#class CategoryCreateView(CreateView):
    # model= Category
    # template_name= 'cupcake_site/add_category.html'
    # fields= ('name',)   
    # def get_initial(self, *args, **kwargs):
    #     initial = super(CategoryCreateView, self).get_initial(**kwargs)
    #     initial['name'] = 'Enter a new category name'
    #     return initial
    # def __init__(self, *args, **kwargs):
    #     super(CategoryForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].help_text = "Enter a new Category name"

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

# class BookCreateView(CreateView):
#     template_name = 'books/book-create.html'
#     form_class = BookCreateForm

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def get_initial(self, *args, **kwargs):
#         initial = super(BookCreateView, self).get_initial(**kwargs)
#         initial['title'] = 'My Title'
#         return initial

#     def get_form_kwargs(self, *args, **kwargs):
#         kwargs = super(BookCreateView, self).get_form_kwargs(*args, **kwargs)
#         kwargs['user'] = self.request.user
#         return kwargs

   
#TODO
# def register_profile():
#     return 
# def profile(request):
#   context_dict={}
#   return render(request, 'cupcake_site/profile.html', context= context_dict)