from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginUser.as_view(), name = 'autorization'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('forumpagenews/', views.forumpage, name = 'forumpagenews'),
    path('forumpagepatch/<int:pk>/', views.patch, name = 'forumpagepatch'),
    path('news/<int:pk>/', views.fullnews, name = 'detailnews'),
    path('aboutus/', views.about, name = 'about'),
    path('discuss/', views.discuss, name = 'discuss'),
    path('discuss/<int:pk>/', views.discussiontopic, name = "discussiontopic"),
]   