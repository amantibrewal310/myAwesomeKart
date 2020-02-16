from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index.html')


def blogPost(request):
    return render(request, 'blog/blog_post.html')
