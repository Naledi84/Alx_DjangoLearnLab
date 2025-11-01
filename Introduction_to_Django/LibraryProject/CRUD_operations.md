# CRUD Operations for Book Model

This file summarizes the Create, Retrieve, Update, and Delete operations performed on the `Book` model using Django's ORM via the shell.

---

## ✅ Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output:
# <Book: 1984 by George Orwell (1949)>

## ✅ retrieve

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output:
# ('1984', 'George Orwell', 1949)

## ✅ update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Output:
# 'Nineteen Eighty-Four'

## ✅ delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output:
# <QuerySet []>


