from django.shortcuts import render, redirect

from bands.forms import CustomUserCreationForm


def home_page(request):
    return render(request, 'bands/index.html')


def create_account(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        new_user_form = CustomUserCreationForm(data=request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect('/')
        else:
            return render(request, 'bands/create_account.html', {'form': form})
    else:
        return render(request, 'bands/create_account.html', {'form': form})


def login(request):
    return render(request, 'bands/login.html')
