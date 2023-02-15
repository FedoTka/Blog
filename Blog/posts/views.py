from django.http import HttpResponse
from django.shortcuts import render
from .models import *
def posts_list(request):
    n = {'Vlad', 'Kirill', 'Mark', 'artem', 'Igor'}
    posts = Post.objects.all()
    return render(request, 'posts/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'posts/post_detail.html', context={'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'posts/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'posts/tag_detail.html', context={'tag': tag})