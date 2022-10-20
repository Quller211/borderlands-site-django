from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginUser.as_view(), name = 'autorization'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('forumpage/', views.forumpage, name = 'forumpage'),
]