from django.urls import path
from .views import create_post, view_posts

urlpatterns = [
    path('post/create/', create_post, name='create_post'),
    path('post/', view_posts, name='view_posts'),
]