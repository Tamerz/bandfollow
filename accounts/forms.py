from django import forms
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_create_user_form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('create_account')
        self.helper.add_input(Submit('submit', 'Sign Up'))

    class Meta:
        model = get_user_model()
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
