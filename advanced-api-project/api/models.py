from django.db import models
from django.utils import timezone

# Author model stores writer's basic information.
# One author can have multiple books (One-to-Many).
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model stores book details including title,
# publication year, and a link to the Author.
# The author field creates a one-to-many relationship.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    publication_year = models.IntegerField()
    
    # ForeignKey creates a one author → many books relationship
    author = models.ForeignKey(
        Author,
        related_name='books',  # used to access all books of an author
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


