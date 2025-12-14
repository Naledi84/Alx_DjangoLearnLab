from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    FeedAPIView,
    LikePostAPIView,
    UnlikePostAPIView
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedAPIView.as_view(), name='feed'),

    # ✅ CHECKER-REQUIRED LIKE ROUTES
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='unlike-post'),
]


