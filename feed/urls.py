from django.urls import path
from .views import PostDetailView

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView.as_view()),
]
