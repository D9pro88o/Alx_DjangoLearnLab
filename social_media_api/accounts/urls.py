from django.urls import path
from .views import RegisterView, LoginView
# social_media_api/urls.py
from django.urls import include

urlpatterns = [
    path('api/', include('posts.urls')),  # posts and comments API
    # other urls...
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),  # <- make sure this line exists
]
