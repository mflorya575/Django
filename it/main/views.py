from django.shortcuts import render
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
