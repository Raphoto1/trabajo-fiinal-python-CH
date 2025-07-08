from django.urls import path, include
from .views import home, all_blogs

urlpatterns = [
    path('', home, name='blog_home'),
    path('all_blogs/', all_blogs, name='all_blogs'),
]