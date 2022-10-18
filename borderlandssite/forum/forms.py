from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Пароль'}))


class RegisterUserForm(UserCreationForm):

        username = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()
