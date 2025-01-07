from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

class SignupView(CreateView):
    """
    Handles user signup functionality.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')  # Redirect to login page after successful signup
    template_name = 'registration/signup.html'

class LoginView(AuthLoginView):
    """
    Handles user login functionality.
    """
    template_name = 'registration/login.html'
