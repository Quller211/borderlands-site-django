from django.shortcuts import render
from .forms import LoginUserForm
from django.contrib.auth.views import LoginView

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/mainpage.html'