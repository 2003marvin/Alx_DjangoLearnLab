# CREATE

from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
# Output:
# <Book: 1984 by George Orwell>
