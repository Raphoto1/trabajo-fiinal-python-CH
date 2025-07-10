from django.shortcuts import HttpResponse, render
from .models import Blog
from .forms import CreateBlogEntryForm
from django.http import HttpResponseRedirect

# Create your views here.

def test(request):
    return HttpResponse('Hola este es un test')

def home(request):
    return render(request, 'blog_manager/home.html')

def all_blogs(request):
    return render(request, 'blog_manager/all_blogs.html')

def create_blog_entry(request):
    if request.method == "POST":
        form = CreateBlogEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            blog = Blog(title=title, content=content)
            blog.save()
            return HttpResponseRedirect('/blogs/')
    else:
        form = CreateBlogEntryForm()
    return render(request, 'blog_manager/create_blog_entry.html', {'form': form})
