"""
Views for Blog application.
"""
from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    """Full blog list"""
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    """Render concrete blog"""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
