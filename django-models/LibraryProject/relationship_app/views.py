from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
<<<<<<< HEAD
=======
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
>>>>>>> 5ad4e561923878743f2ab283f86ff092cdbcf213

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
<<<<<<< HEAD

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
=======
    
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
>>>>>>> 5ad4e561923878743f2ab283f86ff092cdbcf213
