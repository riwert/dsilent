from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'title': 'Posts',
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)

def show(request, id):
    posts = Post.objects.all().exclude(id=id).order_by('-created_at')[:10]
    post = Post.objects.get(id=id)

    context = {
        'title': 'Other posts',
        'posts': posts,
        'post': post,
    }

    return render(request, 'posts/show.html', context)
