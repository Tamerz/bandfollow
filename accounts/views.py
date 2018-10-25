from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import LoginForm, CustomUserCreationForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return redirect('/')
    else:
        return render(request, 'accounts/../static/registration/login.html', {'form': LoginForm()})


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
