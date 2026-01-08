from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from rest_framework.filters import OrderingFilter  # Added OrderingFilter import
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'books/book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'books/book_form.html'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'


 # Enable filtering, searching, and ordering
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

