from django.contrib import admin

# Register your models here.
from .models import Blog

register_models = [Blog]

admin.site.register(register_models)
