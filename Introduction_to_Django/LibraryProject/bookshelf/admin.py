from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('publication_year', 'author')            # Add filters
    search_fields = ('title', 'author')                     # Enable search

admin.site.register(Book, BookAdmin)


