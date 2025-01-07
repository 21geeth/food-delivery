# accounts/urls.py
from django.urls import path
from .views import SignupView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),  # Correct usage for class-based views
    path('login/', LoginView.as_view(), name='login'),
]

  # Import the signup view from the accounts app





