from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    list_filter = ('author', 'publication_year')            # Sidebar filters
    search_fields = ('title', 'author')                     # Search box

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)