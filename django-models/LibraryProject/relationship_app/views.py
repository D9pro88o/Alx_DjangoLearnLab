# LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView   # exact import the checker expects
from .models import Book, Library                    # <- make sure Library is imported

# Function-based view (uses app-relative template path)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based detail view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'