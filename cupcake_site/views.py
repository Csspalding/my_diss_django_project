from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
#from django.utils.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic import CreateView
from django.utils import timezone

from cupcake_site.models import Category, Page, UserProfile
from cupcake_site.forms import CategoryForm, PageForm, UserForm, UserProfileForm, ImageUploadForm
#view handles responce to request from client


#index view is the home page for the project
def index(request):
  #construct a dictionary to pass to the template engin as its context.
  context_dict= {'boldmessage':'did you know... you can learn coding skills for free...'}
  return render(request, 'cupcake_site/index.html', context=context_dict)

#About page
class AboutView(View):
  def get(self, request):
    context_dict={'boldmessage': 'We need more women in tech'}
    #NOT YET tracking visits
    #context_dict = {}
    #context_dict['visits'] = request.session['visits']
    return render(request, 'cupcake_site/about.html', context=context_dict)

#carsole for the About page todo change this
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
  context_dict ={}
  context_dict ['categories'] = category_list
  context_dict ['pages'] = page_list
  return render(request, 'cupcake_site/tools.html', context=context_dict)

#Show links for the selected Learning Tool
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
        form.helper.form_action = reverse('url_name', kwargs={'category_name_slug': category_name_slug})
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

        #To test user authentication    
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
   
#modified from Tango book    
class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
      profiles = UserProfile.objects.all()

      return render(request, 'cupcake_site/list_profiles.html',{'userprofile_list':profiles})


