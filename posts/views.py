#from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    #if the method is Post
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
        else:
           return HttpResponseRedirect(form.erros.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]
    #show
    return render(request, 'posts.html',{'posts':posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
                  