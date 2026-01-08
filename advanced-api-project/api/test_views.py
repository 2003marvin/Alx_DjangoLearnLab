from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book , Author

class BookAPITestCase(TestCase):
    """
    Test case for CRUD operations on the Book model API.
    """

    def setUp(self):
        """Set up test client and sample data."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', author=self.author)
        self.book_url = f'/api/books/{self.book.id}/'
        self.book_list_url = '/api/books/'
        

    def test_create_book(self):
        """Ensure a book can be created successfully."""
        data = {'title': 'New Book', 'author': self.author.id}
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        """Ensure a book can be retrieved successfully."""
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Ensure a book can be updated successfully."""
        new_author = Author.objects.create(name='Updated Author')
        data = {'title': 'Updated Title', 'author': new_author.id}
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        """Ensure a book can be deleted successfully."""
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_book_list(self):
        """Ensure books can be listed successfully."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_unauthenticated_access(self):
        """Ensure unauthenticated users cannot create, update, or delete books."""
        self.client.logout()
        data = {'title': 'Unauthorized Book', 'author': self.author.id}
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filtering_books(self):
        """Test book filtering functionality."""
        response = self.client.get(f'{self.book_list_url}?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

if __name__ == '__main__':
    TestCase.main()
