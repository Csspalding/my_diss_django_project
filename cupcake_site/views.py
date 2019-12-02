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
from cupcake_site.forms import CategoryForm, PageForm, UserForm, UserProfileForm, ImageUploadForm



"""index view is the home page for the web application site"""

class IndexView(View):
  """construct a dictionary to pass to the template html as its context or data to be rendered."""
  def get(self, request):
    context_dict= {'boldmessage':'did you know... you can learn coding skills for free...'}
    return render(request, 'cupcake_site/index.html', context=context_dict)

"""About page"""
class AboutView(View):
  def get(self, request):
    context_dict={}
    return render(request, 'cupcake_site/about.html', context=context_dict)

#carsole for the About page todo change this name and position
def h(request):
  context_dict={'boldmessage': 'We need more women in tech'}
  return render(request, 'cupcake_site/h.html', context=context_dict)


#Learning Tools Categories Page 
def tools(request):
  #get all the categories, later maximum 10 [:10]
  category_list = Category.objects.all()#can order by likes
  page_list = Page.objects.order_by('views')[:5]
  #category_list = Category.objects.order_by('-likes')[:5]
  #save them
  #NOT YET tracking visits
    #context_dict = {}
    #context_dict['visits'] = request.session['visits']
  context_dict ={}
  context_dict ['categories'] = category_list
  context_dict ['pages'] = page_list
  return render(request, 'cupcake_site/tools.html', context=context_dict)

#Show links for the selected Learning Tool
#TODO write def create_context_dic for this class
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

#Add another link to a Learning Tool category
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

        #form.helper.form_action = reverse('url_name', kwargs={'category_name_slug': category_name_slug})
        
        return redirect(reverse('cupcake_site:show_category', kwargs={'category_name_slug':category_name_slug}))
        #return show_category(request, category_name_slug)
    else:
      print(form.errors)

  context_dict = { 'form':form, 'category':category } #objects passed through the template context dictionary to the html
  return render(request, 'cupcake_site/add_page.html', context=context_dict)

     
#Class to create and process the Form to add a new Category to Learning Tools       
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

# Create User Profile Form, assumes a user has signed up and created a django.contrib.auth.models.User instance prior
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
        #allows user to upload data user's profile 
        user_profile.user = request.user 
        user_profile.save()# saves the new data attributes to the userprofile
        form.helper.include_media = True
        return redirect('cupcake_site:index')
        
      else:
        print(form.errors)
    
      return render(request, 'cupcake_site/profile_registration.html', {'form': form}) 

#allow a registered user to view and amend their profile
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
                              #'web' :userprofile.web,
                              #'coding_level':userprofile.coding_level,
                              #'tech_interests':userprofile.tech_interests,
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

        #To test if user is authenticated    
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
   
    
class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
      profiles = UserProfile.objects.all()

      return render(request, 'cupcake_site/list_profiles.html',{'userprofile_list':profiles})

"""Cookies and Likes """
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

class GotoView(View):
    def get(self, request):
        page_id = request.GET.get('page_id')
        
        try:
            selected_page = Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            return redirect(reverse('rango:index'))
            
        selected_page.views = selected_page.views + 1
        selected_page.last_visit = timezone.now()
        selected_page.save()
        
        return redirect(selected_page.url)

class LikeCategoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        category_id = request.GET['category_id']
        
        try:
            category = Category.objects.get(id=int(category_id))
        except Category.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        category.likes = category.likes + 1
        category.save()
        
        return HttpResponse(category.likes)

# def get_category_list(max_results=0, starts_with=''):
#     category_list = []
    
#     if starts_with:
#         category_list = Category.objects.filter(name__istartswith=starts_with)
    
#     if max_results > 0:
#         if len(category_list) > max_results:
#             category_list = category_list[:max_results]
    
#     return category_list

# class CategorySuggestionView(View):
#     def get(self, request):
#         suggestion = request.GET['suggestion']
#         category_list = get_category_list(max_results=8, starts_with=suggestion)
        
#         if len(category_list) == 0:
#             category_list = Category.objects.order_by('-likes')
        
#         return render(request, 'rango/categories.html', {'categories': category_list})

# # View added for the Add button when adding a page to a category.
# class SearchAddPageView(View):
#     @method_decorator(login_required)
#     def get(self, request):
#         category_id = request.GET['category_id']
#         title = request.GET['title']
#         url = request.GET['url']
        
#         try:
#             category = Category.objects.get(id=int(category_id))
#         except Category.DoesNotExist:
#             return HttpResponse('Error - category not found.')
#         except ValueError:
#             return HttpResponse('Error - bad category ID.')
        
#         p = Page.objects.get_or_create(category=category,
#                                        title=title,
#                                        url=url)
        
#         pages = Page.objects.filter(category=category).order_by('-views')
#         return render(request, 'rango/page_listing.html', {'pages': pages})



