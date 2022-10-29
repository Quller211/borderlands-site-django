from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import News, Borderlandspatch, Category, DiscussionTopic

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/mainpage.html'
    next_page = 'forumpagenews'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    next_page = 'autorization'

def forumpage(request):
    data = News.objects.all()
    patches = Category.objects.all()
    return render(request, 'main/forumpagenews.html', {'data' : data, 'patches' : patches})

def patch(request, pk):
    data = Borderlandspatch.objects.filter(cat_id = pk)
    patches = Category.objects.all()
    return render(request, 'main/forumpagepatch.html', {'data': data, 'patches' : patches})

class FullNews(DetailView):
    model = News
    template_name = 'main/news_detail.html'

def about(request):
    patches = Category.objects.all()
    return render(request, 'main/aboutus.html', {'patches' : patches})

def discuss(request):
    data = DiscussionTopic.objects.all()
    patches = Category.objects.all()
    return render(request, 'main/discuss.html', {'data': data, 'patches' : patches})