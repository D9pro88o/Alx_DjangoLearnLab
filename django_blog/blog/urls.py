from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', views.tagged_posts, name='tagged-posts'),
    # your existing post URLs...
]
