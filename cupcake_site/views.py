from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic import CreateView
from django.utils import timezone
from datetime import datetime
from django.utils import timezone

from cupcake_site.models import Category, Page, UserProfile
from cupcake_site.forms import CategoryForm, PageForm, UserProfileForm

"""
Cassie Spalding 2140148s 
Code for the view's adapted and guided by Azzopardi & Maxwell "Tango with Django" (2019)"""

"""index view is the Home page for the web application site"""
class IndexView(View):
  """construct a dictionary to pass to the template html as its context for data to be rendered."""
  def get(self, request):
    return render(request, 'cupcake_site/index.html')

"""About page"""
class AboutView(View):
  def get(self, request):
    context_dict={}
    return render(request, 'cupcake_site/about.html', context=context_dict)

"""Career carsousel"""
def career(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/career.html', context=context_dict)


"""Learning Tools Categories Page"""
def tools(request):
  """display all the categories in a list, to only show a  maximum 10  use [:10]"""
  category_list = Category.objects.all()
  page_list = Page.objects.order_by('views')[:5]
  
  context_dict ={}
  context_dict ['categories'] = category_list
  context_dict ['pages'] = page_list
  visitor_cookie_handler(request)
  context_dict['visits'] = request.session['visits']
  return render(request, 'cupcake_site/tools.html', context=context_dict)

"""Display a list of links for the selected Learning Tool"""
#TODO write def create_context_dic for this class"""
def show_category(request, category_name_slug):
  context_dict={}
  try:
    # get method returns DoesNotExist or instance // try/catch  handles exception if no categories exist
    category= Category.objects.get(slug=category_name_slug)
    # filter method  return a list of page objects or an empty list
    pages= Page.objects.filter(category=category)
    # Save results from filter 
    context_dict['pages'] = pages
    # add the category object from database to the context dictionary, which is used to verify it exists in the template 
    context_dict['category']= category
  except Category.DoesNotExist:
    # set context_dict to None as none found, DoesNotExist exception is displayed
    context_dict['pages'] = None 
    context_dict['category']= None 
  return render(request, 'cupcake_site/tools_category.html', context=context_dict)

"""Add a page link to a specified Learning Tool category"""
# the slug eliminates white spaces in URL, is the title of the category passed in
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
    #once page form is created, check it has a valid category 
    #category_name_slug passed in parameter, by providing a value in dictionary as kwargs to the reverse function, Django can formulate the url
        return redirect(reverse('cupcake_site:show_category', kwargs={'category_name_slug':category_name_slug}))
    else:
      print(form.errors)

  context_dict = { 'form':form, 'category':category } 
  return render(request, 'cupcake_site/add_page.html', context=context_dict)
    
"""Form to Add a new Category to Learning Tools and process"""       
class CategoryCreateView(CreateView):
    @method_decorator(login_required)
    def get(self, request):
      form=CategoryForm()
      return render(request, 'cupcake_site/add_category.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
      form= CategoryForm(request.POST)

      if form.is_valid():
        form.save(commit=True)
        return tools(request)
      else:
        print(form.errors)
      return render(request, 'cupcake_site/add_category.html', {'form': form})  

"""Create a User Profile, assumes a user has signed up and created a django.contrib.auth.models.User instance prior"""
class RegisterProfileCreateView(CreateView):
    @method_decorator(login_required)
    def get(self, request):
      form=UserProfileForm()
      return render(request, 'cupcake_site/profile_registration.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
      form=UserProfileForm(request.POST, request.FILES)

      if form.is_valid():
        user_profile = form.save(commit=False)#creates user profile instance, but does not save it
        #allows user to upload data and maps profile to user registered 
        user_profile.user = request.user 
        user_profile.save()# saves the new data attributes to the userprofile
        form.helper.include_media = True
        #redirect index page
        return redirect ('cupcake_site:index')
        
      else:
        print(form.errors)
    
      return render(request, 'cupcake_site/profile_registration.html', {'form': form}) 

"""Display a registered users profile, allow a registered user to view and amend their profile"""
class ProfileCreateView(CreateView):
    def get_user_details(self, username):
      try:
          user = User.objects.get(username=username)
      except User.DoesNotExist:
          return None
      
      userprofile = UserProfile.objects.get_or_create(user=user)[0]
      include_media = True
      form = UserProfileForm({'bio': userprofile.bio,
                              'email':userprofile.email,
                              'picture': userprofile.picture})
      return (user, userprofile, form)
  

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)    
        except TypeError:
            return redirect('cupcake_site:index')
        
        context_dict = {'userprofile': userprofile,
                        'selecteduser': user,
                        'form': form,
                        }
        form.helper.include_media = True
        return render(request, 'cupcake_site/profile.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, userprofile, form) = self.get_user_details(username)
        except TypeError:
            return redirect('cupcake_site:index')

        #To test if user is authenticated this is a second check, method decorator already checks this.   
        if user == request.user:
            form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
  
            if form.is_valid():
              form.save(commit=True)
              form.helper.include_media = True
              return redirect('cupcake_site:profile', user.username)

            else:
                print(form.errors)

            context_dict = {'userprofile': userprofile,
                            'selecteduser': user,
                            'form': form}
        form.helper.include_media = True
        return render(request, 'cupcake_site/profile.html', context_dict)
   
"""Allow a user to see a list of Members"""    
class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
      profiles = UserProfile.objects.all()

      return render(request, 'cupcake_site/list_profiles.html',{'userprofile_list':profiles})

"""Cookies and Visits  """
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    
    if not val:
        val = default_val
    
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

