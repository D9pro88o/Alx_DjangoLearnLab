from django.urls import path
from .views import PostByTagListView

urlpatterns = [
    # existing URLs...
    path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
