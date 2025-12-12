from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")
print(book)  # Output should display book details