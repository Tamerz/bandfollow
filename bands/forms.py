from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'password1', 'password2', 'email'
        ]
