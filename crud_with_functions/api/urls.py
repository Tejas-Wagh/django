from django.urls import path
from .views import getALlPosts, getPost, createPost, updatePost, deletePost

urlpatterns = [
    path('posts/', getALlPosts),
    path('post/<int:id>/',getPost),
    path('post/create/',createPost),
    path('post/update/<int:id>/',updatePost),
    path('post/delete/<int:id>/', deletePost),
]

