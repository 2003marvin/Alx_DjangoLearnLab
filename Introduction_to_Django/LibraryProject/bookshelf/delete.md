# Delete Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
books = Book.objects.all()
print(books)  # Output should confirm the book is removed