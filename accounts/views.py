from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserCreationForm


def login(request):
    return render(request, 'accounts/login.html', {'form': LoginForm()})


def create_account(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        new_user_form = CustomUserCreationForm(data=request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect('/')
        else:
            return render(request, 'accounts/create_account.html', {'form': form})
    else:
        return render(request, 'accounts/create_account.html', {'form': form})
