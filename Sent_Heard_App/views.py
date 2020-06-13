from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy

from .forms import DeactivateUserForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def donate(request):
    return render(request, "donate.html")

def about_us(request):
    return render(request, "about_us.html")

def yourAccount(request):
    return render(request, "yourAccount.html")


def delete_user(request):
    return render(request, "account/deactive-status.html")

# def delete_user_confirm(request):
#     user = User
#     user.is_active = False
#     user.save()
#     return render(request, "account/account-deleted.html")

def delete_user_confirm(request):
    user = request.user
    user.is_active = False
    user.save()
    return render(request, "account/account-deleted.html")

# login_required(login_url='/accounts/login/')



