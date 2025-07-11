from django import forms
from .models import Blog, Post, Comment

class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=200, label='Título')
    topic = forms.CharField(max_length=100, required=False, label='Tema')
    content = forms.CharField(widget=forms.Textarea, label='Contenido')
    author = forms.CharField(max_length=100, label='Autor')

    def save(self):
        blog = Blog(
            title=self.cleaned_data['title'],
            topic=self.cleaned_data['topic'],
            content=self.cleaned_data['content'],
            author=self.cleaned_data['author']
        )
        blog.save()
        return blog
    
class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=200, label='Título')
    content = forms.CharField(widget=forms.Textarea, label='Contenido')
    author = forms.CharField(max_length=100, label='Autor')

    def save(self):
        post = Post(
            title=self.cleaned_data['title'],
            content=self.cleaned_data['content'],
            author=self.cleaned_data['author']
        )
        post.save()
        return post
    
class CreateCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='Contenido')
    author = forms.CharField(max_length=100, label='Autor')

    def save(self, post):
        comment = Comment(
            post=post,
            content=self.cleaned_data['content'],
            author=self.cleaned_data['author']
        )
        comment.save()
        return comment