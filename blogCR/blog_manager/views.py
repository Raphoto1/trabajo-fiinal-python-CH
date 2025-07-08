from django.shortcuts import HttpResponse, render
from .models import Blog

# Create your views here.

def test(request):
    return HttpResponse('Hola este es un test')

def home(request):
    return render(request, 'blog_manager/home.html')

def all_blogs(request):
    return render(request, 'blog_manager/all_blogs.html')

def create_blog_entry(request):
    pass