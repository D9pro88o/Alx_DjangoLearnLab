from django.urls import path, include

urlpatterns = [
    path('api/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/accounts/', include('accounts.urls')),
]
