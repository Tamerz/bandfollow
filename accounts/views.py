from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .forms import LoginForm, CustomUserCreationForm


def login(request):
    if request.method == 'POST':
        return redirect('/')
    else:
        return render(request, 'accounts/login.html', {'form': LoginForm()})


def logout(request):
    auth_logout(request)
    return redirect('/')


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
