from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


# Serializer for Book model.
# Converts Book model instances to JSON format and vice versa.
class BookSerializer(serializers.ModelSerializer):

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = '__all__'  # serialize all fields of Book model


# Serializer for Author model.
# Includes nested books using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: shows all books for the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        # `books` comes from related_name='books' in Book model
