from typing import Dict, List
from django.shortcuts import render
from .models import Post


posts: List[Dict[str, str]] = [
    {
        'author': 'Andrew',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 12, 2019'
    },
    {
        'author': 'Bob the builder',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 12, 2019'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

