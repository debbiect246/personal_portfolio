from django.shortcuts import render
from .models import Blog

# view for blog page


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
