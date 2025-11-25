from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# PERMISSIONS:
# Read-only for everyone, Write actions for authenticated users only.
class BookPermission(permissions.BasePermission):
    """
    Custom permission:
    - SAFE METHODS (GET, HEAD, OPTIONS) allowed for anyone
    - POST, PUT, DELETE allowed only for authenticated users
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


# LIST + CREATE VIEW
class BookListView(generics.ListCreateAPIView):
    """
    Handles:
    - GET /books/  => list all books
    - POST /books/ => create new book (auth required)
    Includes filtering, searching and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BookPermission]

    # Filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter fields
    filterset_fields = ["title", "publication_year", "author"]

    # Search fields
    search_fields = ["title", "author__name"]

    # Ordering fields
    ordering_fields = ["title", "publication_year"]


# DETAIL VIEW (Retrieve, Update, Delete)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles:
    - GET /books/<pk>/
    - PUT /books/<pk>/ (auth required)
    - DELETE /books/<pk>/ (auth required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BookPermission]
