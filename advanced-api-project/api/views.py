# api/views.py
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# List all books with filtering, search and ordering support.
# - Unauthenticated users: read-only access (IsAuthenticatedOrReadOnly)
# - Filtering via ?title=... or ?publication_year=...
# - Search via ?search=keyword (searches title and author__name)
# - Ordering via ?ordering=title or ?ordering=-publication_year
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # enable DjangoFilterBackend, SearchFilter, OrderingFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # fields filterable with ?field=value
    filterset_fields = ['title', 'publication_year', 'author__name']

    # fields searched with ?search=keyword
    search_fields = ['title', 'author__name']

    # fields allowed in ?ordering=
    ordering_fields = ['title', 'publication_year', 'author__name']


# Retrieve a single book (readable by anyone; use same permission)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
