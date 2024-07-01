from django.shortcuts import render


def index(request):

    context = {
        'title': 'Главная',
    }

    return render(request, 'main/index.html', context)


def blog(request):

    context = {
        'title': 'Блог',
    }

    return render(request, 'main/blog.html', context)
