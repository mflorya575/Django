from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):

    context = {
        'title': 'Главная',
    }

    return render(request, 'main/index.html', context)


def blog(request):
    posts = Post.objects.all()

    context = {
        'title': 'Блог',
        'posts': posts
    }

    return render(request, 'main/blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'title': post.title,
        'post': post,
    }

    return render(request, 'main/blog_detail.html', context)
