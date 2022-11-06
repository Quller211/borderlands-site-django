from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Commentary, Discussions

class LoginUserForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Пароль'}))


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ['text']
        widgets = {
            'text' : forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Добавить запись', 'rows' : 3, 'cols' : 5}),
        }

class AddDiscussion(forms.ModelForm):

    class Meta:
        model = Discussions
        fields = ['field_text']
        widgets = {
            'field_text': forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Добавить запись', 'rows' : 3, 'cols' : 5})
        }