from django.urls import path
from .views import BooksListCreateView, BookDetailView


urlpatterns = [
    path("",BooksListCreateView.as_view()),
    path("book/<int:id>/",BookDetailView.as_view())
]