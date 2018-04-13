from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category, Tag

# Create your views here.
POSTS_LIMIT = 5

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    tags = Tag.objects.all().order_by('name')

    paginator = Paginator(posts, POSTS_LIMIT)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title': 'Posts',
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'posts_limit': POSTS_LIMIT,
    }

    return render(request, 'posts/index.html', context)

def show(request, slug):
    posts = Post.objects.all().exclude(slug=slug).order_by('-created_at')[:10]
    post = Post.objects.get(slug=slug)

    context = {
        'title': 'Other posts',
        'posts': posts,
        'post': post,
    }

    return render(request, 'posts/show.html', context)

def category(request, slug):
    if slug == 'none':
        category = None
        posts = Post.objects.all().filter(category=category).order_by('-created_at')
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.all().filter(category=category).order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    tags = Tag.objects.all().order_by('name')

    paginator = Paginator(posts, POSTS_LIMIT)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title': category.name if category else 'Without category',
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'posts/index.html', context)

def tag(request, slug):    
    tag = Tag.objects.get(name=slug)
    posts = Post.objects.all().filter(tags=tag).order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    tags = Tag.objects.all().order_by('name')

    paginator = Paginator(posts, POSTS_LIMIT)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title': '#' + tag.name,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'posts/index.html', context)
