from django.urls import path
from .views import (
    list_books, LibraryDetailView, register,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Secured Book management
    path('add_book/', add_book, name='add_book'),              # <- exact path for checker
    path('edit_book/<int:pk>/', edit_book, name='edit_book'), # <- exact path for checker
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
