
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import reverse
#from app.models import Page
from posts.models import Posts
#from posts.models import Comment
#from app.forms import PageForm
#from datetime import datetime



# class PostsList(generic.ListView):
#     queryset = Posts.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostsDetail(generic.DetailView):
#     model = Posts
#     template_name = 'post_detail.html'


def posts_index(request):
    #return HttpResponse('Hello from Posts') #USE THIS FIRST to test page link works  - restful API
    
    # to bring in data, the model is imported above see .models import Posts 
    #posts= Posts.objects.all()[:20] # this specifies a max 20 first/recent Post or Blog objects from the model Posts
    #return render(request, 'posts/index.html')
   

    #a neater way of writing the above is to wrap in a variable convention often calls 'context' or 'data'

    posts= Posts.objects.all()[:10] #gets the first 10 posts
    context = {
        'title':'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/posts_index.html', context)


def posts_details(request, id):
    post = Posts.objects.get(id=id)
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

    context = {
        'post': post,

        }
    return render(request, 'posts/posts_details.html', context)

#class PostDetailsCreateView(CreateView):

# def get_user_details(self, username):
#       try:
#           user = User.objects.get(username=username)
#       except User.DoesNotExist:
#           return None
      
#       userprofile = UserProfile.objects.get_or_create(user=user)[0]
#  @method_decorator(login_required)
#     def get(self, request, username):
#         try:
#             (user, userprofile, form) = self.get_user_details(username)    
#         except TypeError:
#             return redirect('cupcake_site:index')
        
#         context_dict = {'userprofile': userprofile,
#                         'selecteduser': user,
#                         'form': form,
#                         }