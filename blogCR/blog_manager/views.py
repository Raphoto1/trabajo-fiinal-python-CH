from django.shortcuts import HttpResponse, render, redirect
from .models import Blog, Post, Comment
from .forms import CreateBlogForm, CreatePostForm, CreateCommentForm

# Create your views here.

def test(request):
    return HttpResponse('Hola este es un test')

def home(request):
    posts = Post.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'blog_manager/home.html', {'posts': posts, 'blogs': blogs})

def all_blogs(request):
    if request.method == 'GET':
        title = request.GET.get('title', '')
        if title:
            blogs = Blog.objects.filter(title__icontains=title)
            return render(request, 'blog_manager/all_blogs.html', {'blogs': blogs})
    blogs = Blog.objects.all()
    return render(request, 'blog_manager/all_blogs.html', {'blogs': blogs})

def all_posts(request):
    if request.method == 'GET':
        title = request.GET.get('title', '')
        if title:
            posts = Post.objects.filter(title__icontains=title)
            return render(request, 'blog_manager/all_posts.html', {'posts': posts})
    posts = Post.objects.all()
    return render(request, 'blog_manager/all_posts.html', {'posts': posts})

def all_comments(request):
    if request.method == 'GET':
        title = request.GET.get('title', '')
        if title:
            comments = Comment.objects.filter(content__icontains=title)
            return render(request, 'blog_manager/all_comments.html', {'comments': comments})
    comments = Comment.objects.all()
    return render(request, 'blog_manager/all_comments.html', {'comments': comments})

def create_blog(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            blog = Blog(
                title=title,
                topic=form.cleaned_data['topic'],
                content=content,
                author=form.cleaned_data['author']
            )
            blog.save()
            return redirect('all_blogs')
    else:
        form = CreateBlogForm()
    return render(request, 'blog_manager/create_blog.html', {'form': form})

def create_Post(request, blog_id):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            blog= Blog.objects.get(id=blog_id)
            post = Post(
                blog=blog,
                title=title,
                content=content,
                author=form.cleaned_data['author']
            )
            post.save()
            return redirect('all_blogs')
    else:
        form = CreatePostForm()
    return render(request, 'blog_manager/create_post.html', {'form': form})

def create_comment(request, post_id):
    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            post = Post.objects.get(id=post_id)
            comment = Comment(
                post=post,
                content=content,
                author=author
            )
            comment.save()
            return redirect('all_posts')
    else:
        form = CreateCommentForm()
    return render(request, 'blog_manager/create_comment.html', {'post_id': post_id, 'form': form})