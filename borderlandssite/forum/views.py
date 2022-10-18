from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, UpdateView, CreateView

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/mainpage.html'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'