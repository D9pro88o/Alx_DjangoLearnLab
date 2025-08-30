from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,
    PostSearchListView
)

urlpatterns = [
    # Blog post URLs
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post detail
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Add comment to post
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Update comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete comment

    # Tag URLs
    path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='posts-by-tag'),  # Filter posts by tag

    # Search URL
    path('search/', PostSearchListView.as_view(), name='post-search'),  # Search posts by title, content, or tags
]
