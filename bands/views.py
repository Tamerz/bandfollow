from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def home_page(request):
    return render(request, 'bands/index.html')


def create_account(request):
    form = UserCreationForm()
    return render(request, 'bands/create_account.html', {'form': form})
