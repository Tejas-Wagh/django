from django.urls import path
from .views import StudentDetailView,StudentListCreateView

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('student/<int:id>/', StudentDetailView.as_view())
]