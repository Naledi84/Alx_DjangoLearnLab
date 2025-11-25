from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        # create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # create authors
        self.author1 = Author.objects.create(name="Charles Dickens")
        self.author2 = Author.objects.create(name="Herman Melville")

        # create books
        self.book1 = Book.objects.create(
            title="A Tale of Two Cities",
            author=self.author1,
            publication_year=1859
        )
        self.book2 = Book.objects.create(
            title="Moby Dick",
            author=self.author2,
            publication_year=1851
        )

        # URLs from your api/urls.py
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.pk])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book1.pk])
        self.delete_url = reverse("book-delete", args=[self.book1.pk])

    # -----------------------------------------------------------
    # LIST VIEW TESTS — List, Search, Filter, Order
    # -----------------------------------------------------------

    def test_can_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Tale"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "A Tale of Two Cities")

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Herman Melville"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["author"], "Herman Melville")

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Moby Dick")  # 1851 comes first

    # -----------------------------------------------------------
    # DETAIL VIEW
    # -----------------------------------------------------------

    def test_can_view_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -----------------------------------------------------------
    # CREATE VIEW — Requires Auth
    # -----------------------------------------------------------

    def test_cannot_create_book_without_auth(self):
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": "Author Test",
            "publication_year": 2024,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_create_book_with_auth(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": "Author Test",
            "publication_year": 2024,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -----------------------------------------------------------
    # UPDATE VIEW — Requires Auth
    # -----------------------------------------------------------

    def test_cannot_update_without_auth(self):
        response = self.client.put(self.update_url, {
            "title": "Updated",
            "author": "Test",
            "publication_year": 2000,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_with_auth(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.put(self.update_url, {
            "title": "Updated Title",
            "author": "Charles Dickens",
            "publication_year": 1860,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # -----------------------------------------------------------
    # DELETE VIEW — Requires Auth
    # -----------------------------------------------------------

    def test_cannot_delete_without_auth(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_delete_with_auth(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())
