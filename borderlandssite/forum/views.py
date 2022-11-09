from django.shortcuts import render, redirect
from .forms import LoginUserForm, RegisterUserForm, AddDiscussion, CommentaryForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Discussions, News, Borderlandspatch, Category, DiscussionTopic, Commentary

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


def fullnews(request, pk):
    patches = Category.objects.all()
    data = News.objects.filter(id = pk)
    com = Commentary.objects.filter(number_of_news_id = pk)
    if request.method == 'POST': 
        form = CommentaryForm(request.POST)
        if form.is_valid():
            addcom = form.save(commit = False)
            addcom.user = request.user
            addcom.number_of_news_id = pk
            addcom.save()
            return redirect('detailnews', pk = pk)
    else:
        form = CommentaryForm()
    return render(request, 'main/news_detail.html', {'data': data, 'patches': patches, 'form': form, 'com': com})
# class FullNews(DetailView):
#     model = News
#     template_name = 'main/news_detail.html'

def about(request):
    patches = Category.objects.all()
    return render(request, 'main/aboutus.html', {'patches' : patches})

def discuss(request):
    data = DiscussionTopic.objects.all()
    patches = Category.objects.all()
    return render(request, 'main/discuss.html', {'data': data, 'patches' : patches})

def discussiontopic(request, pk):
    patches = Category.objects.all()
    data = Discussions.objects.filter(distop_id = pk)
    if request.method == 'POST': 
        form = AddDiscussion(request.POST)
        if form.is_valid():
            adddis = form.save(commit = False)
            adddis.user = request.user
            adddis.distop_id = pk
            adddis.save()
            return redirect('discussiontopic', pk = pk)
    else:
        form = AddDiscussion()
    
    return render(request, 'main/discussiontopic.html', {'data': data, 'patches': patches, 'form': form})
