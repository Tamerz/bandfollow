from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from .forms import LoginForm, CustomUserCreationForm
from .tokens import account_activation_token

User = get_user_model()


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return redirect('/')
    else:
        return render(request, 'registration/login.html', {'form': LoginForm()})


def logout(request):
    auth_logout(request)
    return redirect('/')


def create_account(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        new_user_form = CustomUserCreationForm(data=request.POST)
        if new_user_form.is_valid():
            user = new_user_form.save(commit=False)
            user.is_active = False
            user.save()
            mail_subject = 'Activate your BandFollow account.'
            message = render_to_string('accounts/acknowledge_email.html', {
                'user': user,
                'domain': 'bandfollow.com',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = new_user_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            if to_email != 'jimmy.jazz@tamerz.com':  # Don't send emails to this test user
                email.send()
            else:
                print('Not sending to test user jimmy.jazz@tamerz.com')

            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return render(request, 'accounts/create_account.html', {'form': form})
    else:
        return render(request, 'accounts/create_account.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return HttpResponse('Thank you for confirming your email address!')
    else:
        return HttpResponse('Activation link is invalid')


