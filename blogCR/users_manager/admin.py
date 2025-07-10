from django.contrib import admin

# Register your models here.
from .models import blog_writer

register_models = [blog_writer]

admin.site.register(register_models)
