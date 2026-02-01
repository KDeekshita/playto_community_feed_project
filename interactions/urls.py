from django.urls import path
from .views import LikeAPIView, LeaderboardAPIView

urlpatterns = [
    path('like/', LikeAPIView.as_view()),
    path('leaderboard/', LeaderboardAPIView.as_view()),
]
