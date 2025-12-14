from django.urls import path
from .views import (
    UserListAPIView,
    UserDetailAPIView,
    FollowUserAPIView,
    UnfollowUserAPIView,
)

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('follow/<int:pk>/', FollowUserAPIView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserAPIView.as_view(), name='unfollow-user'),
]



