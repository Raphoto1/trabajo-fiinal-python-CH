from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"titulo: {self.title}"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"titulo: {self.title}"
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"Comentario en {self.post.title} por {self.author}"