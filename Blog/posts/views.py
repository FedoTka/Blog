from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import *
from django .shortcuts import redirect
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin
from .forms import ImageForm, PostForm

class post_create_view(View):
    def get(self, request):
            form = PostForm()
            return render(request, 'posts/post_create.html', context = {'form': form})
    def post(self, request):
        bound_form = PostForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'posts/post_create.html', {'form': bound_form})

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'posts/media.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'posts/media.html', {'form': form})



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', context={'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'posts/post_detail.html'
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'posts/tags_list.html', context={'tags': tags})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'posts/tag_detail.html'
