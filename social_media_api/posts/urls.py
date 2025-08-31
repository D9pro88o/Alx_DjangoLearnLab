from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FeedViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('feed', FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
]
