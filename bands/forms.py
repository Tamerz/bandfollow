from django.contrib.auth.forms import UserCreationForm
from django import forms

from bands.models import User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = [
            'username', 'name', 'password1', 'password2', 'email'
        ]


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=100, widget=forms.fields.TextInput(attrs={
            'class': 'form-control',
        }))
    password = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }))


