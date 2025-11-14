from relationship_app.models import Author, Book, Library


def books_by_author(author_name: str):
    """
    Return all books written by the author with the given name.
    """
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


def books_in_library(library_name: str):
    """
    Return all books in the library with the given name.
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()


def librarian_for_library(library_name: str):
    """
    Return the librarian for the library with the given name.
    """
    library = Library.objects.get(name=library_name)
    return library.librarian
