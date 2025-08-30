from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields you can filter directly with query params
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Fields you can search with ?search=keyword
    search_fields = ['title', 'author__name']
    
    # Fields you can order by with ?ordering=title or ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year', 'author__name']
