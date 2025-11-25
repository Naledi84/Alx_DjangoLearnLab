from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# LIST VIEW — Public
# -----------------------------
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# DETAIL VIEW — Public
# -----------------------------
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# CREATE VIEW — Authenticated to modify, read-only for others
# -----------------------------
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


# -----------------------------
# UPDATE VIEW — Authenticated to modify, read-only for others
# -----------------------------
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# -----------------------------
# DELETE VIEW — Authenticated to modify, read-only for others
# -----------------------------
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
