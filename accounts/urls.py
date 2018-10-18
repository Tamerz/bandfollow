from django.urls import path
from accounts import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('create_account', views.create_account, name='create_account'),
]
