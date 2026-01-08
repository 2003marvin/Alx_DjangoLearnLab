# 📘 Advanced API Project

## 📌 Book API Endpoints

### 📜 Public Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/books/` | List all books |
| `GET` | `/books/<int:pk>/` | Get a single book |

### 🔐 Authenticated Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/books/create/` | Add a new book |
| `PUT` | `/books/<int:pk>/update/` | Update a book |
| `DELETE` | `/books/<int:pk>/delete/` | Delete a book |

## 🔑 Authentication
- **Signup/Login** at `/admin/`
- Use **JWT Tokens** for API authentication.

---

Now, commit your changes to GitHub:

```sh
git add .
git commit -m "Implemented DRF Generic Views for Book model"
git push origin main
 

 ✅ Step 1: Install Django Filter
Django REST Framework supports filtering via django-filter, so install it first if you haven't:

sh
Copy
Edit
pip install django-filter
Then, add it to your installed apps in settings.py:

python
Copy
Edit
INSTALLED_APPS = [
    ...
    'django_filters',
]
✅ Step 2: Update views.py for Filtering, Searching & Ordering
Modify your BookListView in api/views.py to integrate DjangoFilterBackend, SearchFilter, and OrderingFilter:

python
Copy
Edit
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Enable filtering by specific fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Enable search by title and author fields
    search_fields = ['title', 'author__name']  # Assuming 'author' is a ForeignKey

    # Enable ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']
✅ Step 3: Update urls.py
Ensure your api/urls.py includes the list view:

python
Copy
Edit
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
]
✅ Step 4: Test API Endpoints
You can now test filtering, searching, and ordering using query parameters:

🛠 Filtering
Get books with a specific title:
bash
Copy
Edit
GET /api/books/?title=The Great Gatsby
Get books by an author:
bash
Copy
Edit
GET /api/books/?author=J.K. Rowling
Get books from a specific year:
bash
Copy
Edit
GET /api/books/?publication_year=2020
🔎 Searching
Search books by title or author (case-insensitive):
sql
Copy
Edit
GET /api/books/?search=Harry
📊 Ordering
Order books by title (A-Z):
bash
Copy
Edit
GET /api/books/?ordering=title
Order books by publication year (oldest to newest):
bash
Copy
Edit
GET /api/books/?ordering=publication_year
Order books by publication year (newest first):
bash
Copy
Edit
GET /api/books/?ordering=-publication_year
