from django.shortcuts import render

from bands.forms import CustomUserCreationForm


def home_page(request):
    return render(request, 'bands/index.html')


def create_account(request):
    form = CustomUserCreationForm()
    return render(request, 'bands/create_account.html', {'form': form})
