from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Book, Library


def list_books(request):
    """
    Lists all books with their authors.
    Renders HTML if template exists; otherwise returns plain text.
    """
    books = Book.objects.select_related('author').all()

    # If you created the template, use it; otherwise return plain text.
    if request.GET.get("html") == "1":
        return render(request, "relationship_app/list_books.html", {"books": books})

    lines = [f"{b.title} by {b.author.name}" for b in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")

class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, including all books in it.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"  # optional template
    context_object_name = "library"

    # Add books to context for convenience (template can use library.books.all too)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.select_related("author").all()
        return context
    
    # Login: use built-in LoginView
class AppLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout: use built-in LogoutView
class AppLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"  # shown if you visit /logout/ directly


# Registration: simple function-based view using UserCreationForm
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration (optional)
            return redirect("list_books")  # or reverse_lazy('list_books')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
