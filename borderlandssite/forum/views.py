from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import News

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/mainpage.html'
    next_page = 'forumpage'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    next_page = 'autorization'

def forumpage(request):
    data = News.objects.all()
    return render(request, 'main/forumpage.html', {'data' : data})