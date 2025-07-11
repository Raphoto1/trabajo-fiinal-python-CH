from django.urls import path, include
from .views import home, all_blogs, create_blog, create_Post, all_posts, create_comment, all_comments

urlpatterns = [
    path('', home, name='blog_home'),
    path('all_blogs/', all_blogs, name='all_blogs'),
    path('all_posts/', all_posts, name='all_posts'),
    path('all_comments/', all_comments, name='all_comments'),
    path('create_blog/', create_blog, name='create_blog'),
    path('create_post/<int:blog_id>/', create_Post, name='create_post'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment'),
]