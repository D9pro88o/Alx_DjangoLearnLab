from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),
]
