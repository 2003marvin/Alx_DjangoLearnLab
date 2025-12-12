# CREATE

from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
# Output:
# <Book: 1984 by George Orwell>


# RETRIEVE

from bookshelf.models import Book
Book.objects.all()

# Output:
# <QuerySet [<Book: 1984 by George Orwell>]>


# Update Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)  # Output: "Nineteen Eighty-Four"


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