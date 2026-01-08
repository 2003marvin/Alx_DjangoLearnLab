from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the BookViewSet for CRUD operations
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define urlpatterns for both ListAPIView and ViewSet
urlpatterns = [
    # Route for listing books using ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router-generated URLs for full CRUD operations
    path('', include(router.urls)),
    
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
