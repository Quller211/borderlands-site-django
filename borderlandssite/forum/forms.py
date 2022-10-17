from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class LoginUserForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Пароль'}))