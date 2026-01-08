import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Function to retrieve all books with their authors
def list_all_books():
    books = Book.objects.all()
    for book in books:
        print(f"Title: {book.title}, Author: {book.author.name}, Published: {book.publication_year}")

# Function to retrieve all books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books:
            print(f" - {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print("Library not found.")

# Function to retrieve a librarian by library
def get_librarian_by_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")

# Function to retrieve books by a specific author
def list_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f" - {book.title} (Published {book.publication_year})")
    except Author.DoesNotExist:
        print("Author not found.")

# Run sample queries
if __name__ == "__main__":
    print("Listing all books:")
    list_all_books()

    print("\nListing books in a specific library:")
    list_books_in_library("Central Library")

    print("\nGetting librarian for a library:")
    get_librarian_by_library("Central Library")

    print("\nListing books by a specific author:")
    list_books_by_author("J.K. Rowling")


