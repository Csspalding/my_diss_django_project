from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse
from django.urls import reverse_lazy

from datetime import datetime

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.forms import PostCreateForm
from django.views import View
from django.views.generic.detail import DetailView
from posts.models import Posts
from django.views.generic.edit import CreateView


"""any user can view a list of titles of published blog posts code adapted from Traversy Media (2017) tutorial "Django crash course" """
def posts_index(request):
    try:
        posts=Posts.objects.all()[:10] #gets the first 10 posts to display
    except Posts.DoesNotExist:
        return None 
    context = {
            'posts': posts
            }
    return render(request, 'posts/posts_index.html', context)

"""allow a registered user to create a new post, adapted from tutorial https://www.agiliq.com/blog/2019/01/django-createview/#using-createview"""

class PostCreate(CreateView):
    template_name = 'posts/posts_create.html'
    form_class = PostCreateForm
    """lazy reverse returns an object, on success of form creation redirect user to the post_index.html page""" 
    success_url = reverse_lazy('posts:posts_index')


    """ Check the user is authenticated, to get the post.user, request the user before the form is saved"""
    @method_decorator(login_required, name='form_valid') 
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        """redirect to the post_index.html page"""
        return HttpResponseRedirect(self.get_success_url()) 

        
    """populate the form body with initial data"""
    def get_initial(self, *args, **kwargs):
        initial = super(PostCreate, self).get_initial(**kwargs)
        initial['body'] = 'My blog post'
        return initial    

    """build keyword arguments to instanticate the form https://docs.djangoproject.com/en/2.2/ref/class-based-views/mixins-editing/"""
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreate, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

"""class to display the view of a single post instance using generic DetailView created adapted from https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/"""
"""no login decorator is required as any user can view post details"""
class PostDetail(DetailView):
    model = Posts
    template_name = 'posts/posts_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, pk=kwargs['pk'])
        context = {'post': post}
        return render(request, 'posts/posts_detail.html', context)