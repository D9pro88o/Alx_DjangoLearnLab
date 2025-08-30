# Delete

```python
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>