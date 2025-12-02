from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostDetail,
    PostList,
    PostUpdateView,
    PostCreateView,
)

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
]

