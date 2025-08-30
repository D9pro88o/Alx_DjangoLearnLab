from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Form for creating or editing Book instances.
    Includes all fields: title, author, publication_year.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # Optional: Add validation to ensure data is safe
    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Example: prevent empty or dangerous input
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Author cannot be empty.")
        return author
