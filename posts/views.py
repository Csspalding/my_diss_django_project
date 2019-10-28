from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import Posts
#from posts.models import Comment
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic import CreateView
from django.utils import timezone

from cupcake_site.models import UserProfile
from posts.models import Posts
#from posts.models import Comments
from posts.forms import PostCreateForm 
#from posts.forms import CommentForm 

#any user can view a list of titles of published blog posts
def posts_index(request):
    try:
        posts=Posts.objects.all()[:10] #gets the first 10 posts 
    except Posts.DoesNotExist:
        return None 
    context = {
            'posts': posts
            }
    return render(request, 'posts/posts_index.html', context)
    #return HttpResponse("hello from posts")

#any user can view the details a published blog post
def posts_details(request, id):
    try:
        post = Posts.objects.get(id=id)
    except Posts.DoesNotExist:
        return None
    context = {
        'post': post,
    }
    return render(request, 'posts/posts_details.html', context)
    #return HttpResponse("hello from posts details")

#modified from https://realpython.com/get-started-with-django-1/ but my posts get id not pk
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

#allow a registered user to create a new post

class PostCreateView(CreateView):
    template_name = 'posts/add_post.html'
    form_class = PostCreateForm
    
    def get_object(self, queryset=None):
      return self.request.user.UserProfile

    def form_valid(self, form):
        form.instance.author_post = self.request.userprofile
        return super(PostCreateView, self).form_valid(form)
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.author_post = self.request.userprofile.username
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(PostCreateView, self).get_initial(**kwargs)
        """populate body with initial data"""
        initial['body'] = 'My blog post'
        return initial
    
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs