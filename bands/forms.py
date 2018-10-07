from django.contrib.auth.forms import UserCreationForm

from bands.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = [
            'username', 'name', 'password1', 'password2', 'email'
        ]
