from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
# Create your views here.
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

# def post_stuff(request):
#     return render(request, "post.html")

# def password_reset(request):
#     return render(request, "/registration/password_reset_form.html")

