
from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import reverse
#from app.models import Page
from .models import Posts
#from app.forms import PageForm
#from datetime import datetime


# Create your views here.



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
    context = {
        'post': post
    }
    return render(request, 'posts/posts_details.html', context)
