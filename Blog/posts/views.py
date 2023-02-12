from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
def posts_list(request):
    n = {'Vlad', 'Kirill', 'Mark', 'artem', 'Igor'}
    posts = Post.objects.all()
    return render(request, 'posts/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    print(post)
    return render(request, 'posts/post_detail.html', context={'post': post})