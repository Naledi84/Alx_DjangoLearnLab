from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Author model: represents a writer with a name and related books
# Book model: includes title, publication year, and foreign key to Author

# BookSerializer: serializes all fields and validates publication_year
# AuthorSerializer: includes nested BookSerializer to show related books
