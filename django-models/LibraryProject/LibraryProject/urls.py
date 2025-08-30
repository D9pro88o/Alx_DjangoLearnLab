from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                 # Admin route
    path('', include('relationship_app.urls')),      # Include app routes
]
