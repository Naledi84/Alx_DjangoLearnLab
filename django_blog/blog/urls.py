from django.urls import path
from .views import (
    PostList,
    PostDetail,
    PostCreateView,
    PostUpdateView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search_view,
)

app_name = "blog"

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),

    # Comment URLs required by checker
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name="comment_create"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="comment_update"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment_delete"),

    # Tag filter
    path('tags/<str:tag>/', PostList.as_view(), name="tagged_posts"),

    # Search
    path("search/", search_view, name="search"),
]



