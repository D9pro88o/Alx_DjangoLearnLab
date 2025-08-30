import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample data creation (optional)
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="Alice", library=library)

# --- Queries ---

# 1. Query all books by a specific author
books_by_author = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", list(books_by_author))

# 2. List all books in a library
library_books = library.books.all()
print(f"Books in {library.name}:", list(library_books))

# 3. Retrieve the librarian for a library
library_librarian = library.librarian
print(f"Librarian for {library.name}:", library_librarian)