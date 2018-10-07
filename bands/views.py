from django.shortcuts import render


def home_page(request):
    return render(request, 'bands/index.html')


def create_account(request):
    return render(request, 'bands/create_account.html')
