from django.urls import path, include
from .views import home, all_blogs, create_blog_entry

urlpatterns = [
    path('', home, name='blog_home'),
    path('all_blogs/', all_blogs, name='all_blogs'),
    path('create_blog_entry/', create_blog_entry, name='create_blog_entry'),
]