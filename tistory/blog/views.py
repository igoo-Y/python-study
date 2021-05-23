from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def detail(request, blog_id):
    # blog = Blog.objects.get(blog_id = id)
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog})
