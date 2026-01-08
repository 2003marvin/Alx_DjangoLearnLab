from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from django.core.exceptions import PermissionDenied
from .forms import ExampleForm

def book_list(request):
    if not request.user.has_perm('bookshelf.can_view'):
        raise PermissionDenied("You do not have permission to view books.")

    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def raise_exception():
    """Raise a PermissionDenied exception for unauthorized access."""
    raise PermissionDenied("You do not have permission to view this page.")

def form_example_view(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Process the data (e.g., save to database)
    
    return render(request, 'bookshelf/form_example.html')