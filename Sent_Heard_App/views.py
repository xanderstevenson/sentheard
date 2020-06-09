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

# def delete_user(request):
#     context = {}

#     try:
#         user = get_user_model()
#         user.is_active = False
#         context['msg'] = 'Profile successfully disabled.'
#     except User.DoesNotExist:
#         pass

#     return render(request, "account/deactive-status.html")

# login_required(login_url='/accounts/login/')
def delete_user(request):

    return render(request, "account/account-deleted.html")
    # else:
    #     raise PermissionDenied

# def post_stuff(request):
#     return render(request, "post.html")

# def password_reset(request):
#     return render(request, "/registration/password_reset_form.html")

