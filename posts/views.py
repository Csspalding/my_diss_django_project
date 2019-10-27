from django.shortcuts import render, redirect
from django.http import HttpResponse
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
from posts.forms import PostForm 
#from posts.forms import CommentForm 


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


class PostCreateView(CreateView):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        if user.is_active:
            posts = Posts.objects.get_or_create(user=user)
            form = PostForm({'title': posts.title,
            'body': posts.body,
            'author_post': user,})
        else:
            redirect()
        return (user, posts, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, post, form) = self.get_user_details(username)    
        except TypeError:
            return redirect('accounts:register')
        
        context_dict = {'post': post,
                        'author_post': user,
                        'form': form,
                        }
        form.helper.include_media = True
        return render(request,'posts/add_post.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, post, form) = self.get_user_details(username)
        except TypeError:
            return redirect('cupcake_site:index')

        #To test user authentication    
        if user == request.user:
            form = PostForm(request.POST, request.FILES, instance=post)
  
            if form.is_valid():
              form.save(commit=True)
              form.helper.include_media = True
              return redirect('posts:posts_home', user.username)

            else:
                print(form.errors)

            context_dict = {'post': post,
                            'selecteduser': user,
                            'form': form}
        form.helper.include_media = True
        return render(request, 'posts/add_post.html', context_dict)
    #todo def post and test user is authentication see cupcake views profilecreateview method