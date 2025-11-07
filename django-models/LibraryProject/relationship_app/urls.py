from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books,
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # 📘 Function-Based View: List All Books
    path('books/', list_books, name='list_books'),

    # 📚 Class-Based View: Library Detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # 🔐 Authentication Views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # 👤 Role-Based Views
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),

    # 📚 Permission-Protected Views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('delete_book/', delete_book, name='delete_book'),
]



