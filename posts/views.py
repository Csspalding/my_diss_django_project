from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse
from django.urls import reverse_lazy

#from posts.models import Comment
from datetime import datetime
from django.utils import timezone

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.forms import PostForm, PostCreateForm
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic.detail import DetailView
from posts.models import Posts
from django.views.generic.edit import CreateView

from cupcake_site.models import UserProfile
#from posts.models import Comments
#from posts.forms import CommentForm 

"""any user can view a list of titles of published blog posts"""
def posts_index(request):
    try:
        posts=Posts.objects.all()[:10] #gets the first 10 posts 
    except Posts.DoesNotExist:
        return None 
    context = {
            'posts': posts
            }
    return render(request, 'posts/posts_index.html', context)
    
#modified from https://realpython.com/get-started-with-django-1/ 
    #comments = Comment.objects.filter(post=post)

    # form = CommentForm()
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = Comment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             post=post
    #         )
    #         comment.save()
        # context = {
        #     'post': post,

        # 'comments': comments,
        # 'form': form

    # context = {
    #     'post': post,

    #     }
    # return render(request, 'posts/posts_details.html', context)

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

    #no longer working    
    """populate the form body with initial data"""
    def get_initial(self, *args, **kwargs):
        initial = super(PostCreate, self).get_initial(**kwargs)
        initial['body'] = 'My blog post'
        return {
            'initial' : initial,
            }
        

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
    #success_url = 

#queryset = Posts.objects.filter(is_published=True)# bool for if the post status is draft or publish, remove model attribute to replace with this? TODO test once view for update post had been coded

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, pk=kwargs['pk'])
        context = {'post': post}
        return render(request, 'posts/posts_detail.html', context)