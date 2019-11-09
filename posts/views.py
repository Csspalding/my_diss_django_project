from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse
from django.urls import reverse_lazy

from posts.models import Posts
#from posts.models import Comment
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DetailView
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
    #try:
    post = Posts.objects.get(id=object.id)
    #except Posts.DoesNotExist:
    #    return None
    context = {
        'post': post
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

#allow a registered user to create a new post, adapted from tutorial https://www.agiliq.com/blog/2019/01/django-createview/#using-createview"""
#correct way to decorate a class, name the function to be decorated.TEST when redirect url is working 
#@method_decorator(login_required, name='form_valid') 

class PostCreateView(CreateView):
    template_name = 'posts/add_post.html'
    form_class = PostCreateForm
    #lazy reverse returns an object
    #success_url = reverse_lazy('posts:posts_details', args=[id])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        #return HttpResponseRedirect(self.get_success_url()) #THIS IS THE PROBLEM LINE
        #return HttpResponseRedirect('/posts/posts_details/'+ str(self.object.id))  #THIS WORKS but page strange page not found error 
        #posts/posts_details/18  - page not to be found! even though url is a match
        return HttpResponse("form is saved")
        #form.helper.form_action = reverse('url_name', kwargs={'id': id})
        #return redirect(reverse('posts:posts_details', kwargs={'pk':self.object.id})
        #HttpRequest.build_absolute_uri()
        #return redirect(reverse('posts:posts_index')) #redirect to post index page once form is saved

       # """populate body with initial data"""
    def get_initial(self, *args, **kwargs):
        initial = super(PostCreateView, self).get_initial(**kwargs)
        initial['body'] = 'My blog post'
        return {
            'initial' : initial,
            }

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

# """class to display the view of a single post instance using generic DetailView created adapted from https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/"""
# #login should be required
# class PostDetailView(DetailView):
#     model = Posts
#     #queryset = Posts.objects.filter(is_published=True)# bool for if the post status is draft or publish, remove model attribute to replace with this
#     def get(self, request, *args, **kwargs):
#         post = get_object_or_404(Posts, pk=kwargs['pk'])
#         context = {'post': post}
#         return render(request, 'posts/posts_details.html', context)