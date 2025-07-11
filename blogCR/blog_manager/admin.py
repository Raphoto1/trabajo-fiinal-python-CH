from django.contrib import admin

# Register your models here.
from .models import Blog, Post, Comment

register_models = [Blog, Post, Comment]

admin.site.register(register_models)
